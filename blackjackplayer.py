from player import Player


class BlackJackPlayer(Player):

    def __init__(self, n):
        super().__init__(n)

    def can_play(self):
        return self.get_player_points() < 21
