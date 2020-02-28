from player import Player


class Dealer(Player):

    def __init__(self, n='None'):
        super().__init__(n)

    def can_play(self):
        return self.get_player_points() <= 16
