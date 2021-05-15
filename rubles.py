from currency import Currency

RUB = 0.013


class Rubles(Currency):
    def __init__(self, money):
        self.money = money

    def to_dollars(self):
        return round(self.money * RUB, 2)


