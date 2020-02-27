from blackjackplayer import BlackJackPlayer
from card import Card
from dealer import Dealer
from deck import Deck
from player import Player


class Table:

    def __init__(self, name: str):
        self.player = BlackJackPlayer(name)
        self.dealer = Dealer('Oberyn')
        self.deck = Deck()
        self.hidden_card = None
        self.turns = []

    def play(self):
        self.hidden_card = self.deck.remove_card()

        self.give_card(self.dealer, self.deck.remove_card())
        self.give_card(self.player, self.deck.remove_card())

        while self.player.can_play() and not self.game_end():
            self.give_card(self.player, self.deck.remove_card())

        if not self.game_end():
            self.give_card(self.dealer, self.hidden_card)
            while self.dealer.can_play() and not self.game_end():
                self.give_card(self.dealer, self.deck.remove_card())

        self.show_winner()

    def give_card(self, p: Player, c: Card):
        self.turns.append((p, c))
        p.add_card(c)
        print(p.get_name() + ' takes card ' + c.get_card_value() + ' for ' + str(c.get_point()[1]))

    def game_end(self):
        if self.player.get_player_points() >= 21:
            return True
        elif self.dealer.get_player_points() >= 21:
            return True
        return False

    def show_winner(self):
        if self.player.get_player_points() >= 21:
            print(self.player.get_name() + ' has lost. ' + str(self.player.get_player_points()) + ' > 21')
        elif self.dealer.get_player_points() >= 21:
            print(self.dealer.get_name() + ' has lost. ' + self.dealer.get_player_points() + ' > 21')
        else:
            winner = self.player if self.player.get_player_points() > self.dealer.get_player_points() else self.dealer
            print(winner.get_name() + ' has won. ' + winner.get_player_points())


if __name__ == '__main__':
    game = Table('Jack')

    print('Welcome to BlackJack. Your dealer will be Oberyn.')
    game.play()
