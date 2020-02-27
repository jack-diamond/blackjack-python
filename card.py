class Card:

    __point: object

    def __init__(self, s, p):
        self.__suit = s
        self.__point = p
        self.suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.points = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), 
                       ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]

    def get_suit(self):
        return self.__suit
    
    def get_point(self):
        return self.__point
