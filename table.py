from blackjackplayer import BlackJackPlayer


class Table:

    def __init__(self, name: str):
        self.player = BlackJackPlayer(name)