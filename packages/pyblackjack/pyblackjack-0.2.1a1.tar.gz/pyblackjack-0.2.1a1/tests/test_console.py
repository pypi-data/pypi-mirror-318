# pylint: disable=wrong-import-order
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=no-member
# pylint: disable=protected-access

import pytest
from io import StringIO
import sys

from pyblackjack import console

def test_error(capfd):
    console.error('Testing.')
    output = capfd.readouterr().out
    assert output == 'Error: Testing. Try again.\n'

def test_get_str(capfd, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', StringIO('\n\n\n   Testing   \n'))
        s = console.get_str('TEST PROMPT: ')
    assert s == 'Testing'
    output = capfd.readouterr().out
    assert output.count('Error:') == 3

def test_get_action(capfd, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', StringIO('x\nd\nw\nu\nHit\ns\n'))
        s = console.get_action('TEST PROMPT', 'hs', 'du')
    assert s == 'h'
    output = capfd.readouterr().out
    assert output.count('Error:') == 4
    lines = output.splitlines()
    assert 'nvalid' in lines[0]
    assert 'chips' in lines[1]
    assert 'nvalid' in lines[2]
    assert 'chips' in lines[3]

@pytest.mark.parametrize('inputs,expected,error', [
    ('y\n', True, None),
    ('x\nyes', True, 'nvalid'),
    ('n\n', False, None),
    ('\nNO\n', False, 'required')
])
def test_get_yes_no(capfd, monkeypatch, inputs, expected, error):
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', StringIO(inputs))
        result = console.get_yes_no('TEST PROMPT:')
    assert result is expected
    output = capfd.readouterr().out
    assert ' [y/n]: ' in output
    if error:
        assert error in output
    else:
        assert 'Error:' not in output

@pytest.mark.parametrize('inputs,args,expected,error', [
    ('42\n', (None, None, None), 42, None),
    ('150\n60\n', (10, 100, None), 60, 'at most'),
    ('5\n25\n', (10, 100, 'q'), 25, 'at least'),
    ('test\n-25\n', (None, None, 'q'), -25, 'nvalid'),
    ('\n0\n', (None, None, None), 0, 'required'),
    ('Q\n', (None, None, 'q'), 'q', None)
])
def test_get_int(capfd, monkeypatch, inputs, args, expected, error):
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', StringIO(inputs))
        result = console.get_int('TEST_PROMPT', *args)
    assert result == expected
    output = capfd.readouterr().out
    if error:
        assert error in output
    else:
        assert 'Error:' not in output
