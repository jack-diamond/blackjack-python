class Card:

    def __init__(self, s='None', p=0):
        self.__suit = s
        self.__point = p

    def get_suit(self):
        return self.__suit
    
    def get_point(self):
        return self.__point

    def get_card_value(self):
        return str(self.get_point()) + ' - ' + self.get_suit()
