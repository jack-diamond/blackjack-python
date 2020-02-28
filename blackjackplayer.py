from player import Player


class BlackJackPlayer(Player):

    def __init__(self, n):
        super().__init__(n)
        self.wants_to_play = True

    def can_play(self):
        return self.get_player_points() < 21

    def get_wants_to_play(self):
        return self.wants_to_play

    def stop_playing(self):
        self.wants_to_play = False
