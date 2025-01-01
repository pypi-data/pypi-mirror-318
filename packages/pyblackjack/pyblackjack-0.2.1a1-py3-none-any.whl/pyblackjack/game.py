import sys
from typing import Final, Literal, NoReturn, Sequence, cast

from . import console
from .objects import SHOE, Hand, Dealer, Player


ACTION_HIT: Final[str] = '[H]it'
ACTION_STAND: Final[str] = '[S]tand'
ACTION_SPLIT: Final[str] = 'S[p]lit'
ACTION_DOUBLE: Final[str] = '[D]ouble down'
ACTION_SURRENDER: Final[str] = 'S[u]rrender'

DIVIDER_LENGTH: Final[int] = 10


class Game:

    def __init__(
        self,
        players: Sequence[str] | None = None,
        chips: int = 1000,
        decks: int = 6,
        hit_soft_17: bool = True,
    ):
        player_list: Sequence[str | None] = ([None] if players is None
                                             else players)
        SHOE.decks = decks
        SHOE.new()
        self.dealer: Final[Dealer] = Dealer(hit_soft_17=hit_soft_17)
        self.players: Final[list[Player]] = [
            Player(name, chips) for name in player_list
        ]
        self.active_players: list[Player] = []

    def mainloop(self) -> None:
        while self.play_hand():
            pass

    def play_hand(self) -> bool:
        self.check_shuffle()
        self.active_players = []
        self.collect_bets()
        if not self.players:
            return False
        self.deal_cards()
        self.print_hands()
        print('-' * DIVIDER_LENGTH)
        if self.check_dealer_blackjack():
            return True
        self.check_player_blackjacks()
        for player in self.active_players.copy():
            self.play_player_hand(player)
        print('-' * DIVIDER_LENGTH)
        if self.active_players:
            self.play_dealer_hand()
            self.pay_winners()
        else:
            self.print_dealer_hand()
        return True

    def collect_bets(self) -> None:
        for player in self.players.copy():
            self.get_bet(player)

    def get_bet(self, player: Player) -> None:
        player.hands = []
        if player.chips == 0:
            print(f'{player.name} is out of chips and is eliminated.')
            self.players.remove(player)
            return
        print(f'{player.name} has {player.chips} chips.')
        bet = cast(int | Literal['q'],
                   console.get_int('Enter a bet, or [q]uit: ', 0, player.chips, 'q'))
        if bet == 'q':
            self.players.remove(player)
            return
        player.bet = bet
        player.chips -= bet
        if bet > 0:
            self.active_players.append(player)
            player.hands.append(Hand(bet=bet))

    def deal_cards(self) -> None:
        for hand in self.active_players + [self.dealer]:
            hand.reset()
        for _ in range(2):
            for hand in self.active_players + [self.dealer]:
                hand.hit()

    def print_hands(self) -> None:
        print('Dealer: ' + self.dealer.print_hand(downcard=True))
        for player in self.active_players:
            print(f'{player.name}: {player.hands[0].print_hand()}')

    def check_dealer_blackjack(self) -> bool:
        if self.dealer.check_insurance():
            self.handle_insurance()
        if self.dealer.check_blackjack():
            self.print_dealer_hand()
            self.resolve_dealer_blackjack()
            return True
        for player in self.active_players:
            if player.insurance:
                player.insurance = False
        return False

    def handle_insurance(self) -> None:
        for player in self.active_players:
            if console.get_yes_no(f'{player.name}: Buy insurance?'):
                player.buy_insurance()

    def resolve_dealer_blackjack(self) -> None:
        print('Dealer has blackjack!')
        for player in self.active_players:
            if player.insurance:
                player.chips += player.insurance * 3
                player.insurance = False
            if player.check_blackjack():
                print(f'{player.name} has blackjack!')
                player.chips += player.bet
        self.active_players.clear()

    def check_player_blackjacks(self) -> None:
        for player in self.active_players.copy():
            if player.check_blackjack():
                print(f'{player.name} has blackjack!')
                player.chips += int(player.bet * 2.5)
                self.active_players.remove(player)

    def play_player_hand(self, player: Player) -> None:
        for _ in player:
            self.play_single_hand(player)
        if all(hand.check_bust() or hand.check_blackjack()
               for _, hand in player):
            self.active_players.remove(player)

    def play_single_hand(self, player: Player) -> None:
        hand: Hand = player.active_hand
        if len(hand.cards) == 1:
            # split hand
            hand.hit()
        while not hand.check_bust():
            name: str = player.get_name()
            print(f'{name}: {hand.print_hand()}')
            if player.is_split() and hand.cards[0] == 1:
                # split aces auto-stand
                break
            if hand.total() == 21:
                # 21 auto-stands
                break
            action: str = self.get_action(player, hand)
            if not self.perform_action(action, player, hand):
                break
        else:
            print(f'{name}: {hand.print_hand()}')
            print(f'{name} busted!')

    @staticmethod
    def get_action(player: Player, hand: Hand) -> str:
        action_list: list[str] = [ACTION_HIT, ACTION_STAND]
        action_check: str = 'hs'
        low_chips_check: str = ''
        if len(hand.cards) == 2:
            if player.check_split():
                if player.check_bet():
                    action_list.append(ACTION_SPLIT)
                    action_check += 'p'
                else:
                    low_chips_check += 'p'
            if player.check_double():
                if player.check_bet():
                    action_list.append(ACTION_DOUBLE)
                    action_check += 'd'
                else:
                    low_chips_check += 'd'
            if not player.is_split():
                action_list.append(ACTION_SURRENDER)
            action_check += 'u'
        actions = ', '.join(action_list) + '? '
        return console.get_action(actions, action_check, low_chips_check)

    def perform_action(self, action: str, player: Player, hand: Hand) -> bool:
        if action == 'h':
            hand.hit()
            return True
        elif action == 's':
            return False
        elif action == 'p':
            player.split()
            return True
        elif action == 'd':
            player.double_down()
            print(f'{player.get_name()}: {hand.print_hand()}')
            return False
        elif action == 'u':
            player.surrender()
            self.active_players.remove(player)
            return False
        else:
            unreachable()

    def play_dealer_hand(self) -> None:
        self.dealer.play_hand()
        self.print_dealer_hand()

    def print_dealer_hand(self) -> None:
        print('Dealer: ' + self.dealer.print_hand())

    def pay_winners(self) -> None:
        for player in self.active_players:
            self.resolve_player_hands(player)

    def resolve_player_hands(self, player: Player) -> None:
        n: int
        hand: Hand
        for n, hand in player:
            msg: str
            if player.is_split():
                msg = f' on hand {n}'
            else:
                msg = ''
            if hand.check_bust():
                continue
            if (self.dealer.check_bust()
                  or hand.total() > self.dealer.total()):
                player.chips += hand.bet * 2
                print(f'{player.name} wins{msg}!')
            elif hand.total() == self.dealer.total():
                player.chips += hand.bet
                print(f'{player.name} pushes{msg}.')
            else:
                print(f'{player.name} loses{msg}.')

    @staticmethod
    def check_shuffle() -> None:
        print('=' * DIVIDER_LENGTH)
        if SHOE.time_to_shuffle:
            SHOE.new()
            print('New shoe in play!')
            print('=' * DIVIDER_LENGTH)

def unreachable() -> NoReturn:
    raise RuntimeError('Unreachable code reached!')

def setup() -> Game:
    numplayers = cast(int | Literal['q'], console.get_int(
        'Enter number of players [1-6] or [q]uickstart: ', 1, 6, 'q'
    ))
    if numplayers == 'q':
        return Game()

    players: list[str] = []
    for n in range(numplayers):
        name: str = console.get_str(f'Enter name for player {n + 1}: ')
        players.append(name)

    chips: int = console.get_int('Enter starting chips: ', min=1)

    decks: int = console.get_int('Enter number of decks in the shoe: ', 1, 8)

    hit_soft_17: bool = console.get_yes_no('Should dealer hit on soft 17?')

    return Game(players, chips, decks, hit_soft_17)


def main() -> int:
    print('Welcome to PyBlackjack!')
    game: Game = setup()
    game.mainloop()
    print('Thanks for playing!')
    return 0


if __name__ == '__main__':
    sys.exit(main())
