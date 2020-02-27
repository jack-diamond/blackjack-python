from card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.points = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
                       ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]
        self.create_deck()
        self.shuffle()

    def create_deck(self) -> None:
        for s in self.suits:
            for p in self.points:
                self.cards.append(Card(s, p))

    def shuffle(self):
        random.shuffle(self.cards)

d = Deck()
print(d.cards)