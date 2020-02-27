class Player:

    def __init__(self, n: str):
        self.__name = n
        self.hand = []

    def get_name(self):
        return self.__name

    def add_card(self, card):
        self.hand.append(card)

    def get_player_points(self):
        min_total = 0
        max_total = 0

        for card in self.hand:
            point = card.get_point()
            min_total += point[1]
            max_total += 11 if point[0] == 'A' else point[1]

        return min_total if max_total > 21 else max_total