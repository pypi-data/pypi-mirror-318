from typing import overload


def error(message: str, /) -> None:
    print(f"Error: {message} Try again.")


def get_str(prompt: str, /) -> str:
    while True:
        s: str = input(prompt).strip()
        if s:
            return s
        else:
            error("Input required.")


def get_action(prompt: str, /, options: str, lowchips: str) -> str:
    while True:
        s: str = get_str(prompt)[0].lower()
        if s in options:
            return s
        elif s in lowchips:
            error("Insufficient chips for that action.")
        else:
            error("Invalid action")


def get_yes_no(prompt: str, /) -> bool:
    while True:
        s: str = get_str(f"{prompt} [y/n]: ").lower()
        if s in {"y", "yes"}:
            return True
        elif s in {"n", "no"}:
            return False
        else:
            error("Invalid input.")


@overload
def get_int(
    prompt: str,
    /,
    min: int | None = None,
    max: int | None = None,
    alt: None = None
) -> int:    ...

@overload
def get_int(
    prompt: str,
    /,
    min: int | None = None,
    max: int | None = None,
    alt: str = ""
) -> int | str:    ...

def get_int(
    prompt: str,
    /,
    min: int | None = None,
    max: int | None = None,
    alt: str | None = None,
) -> int | str:
    while True:
        s: str = get_str(prompt).lower()
        if alt and s.lower() == alt.lower():
            return s.lower()
        try:
            z: int = int(s)
        except ValueError:
            error("Invalid integer.")
            continue
        if min is not None and z < min:
            error(f"Integer must be at least {min}.")
            continue
        if max is not None and max < z:
            error(f"Integer must be at most {max}.")
            continue
        return z
