from currency import Currency


class Dollar(Currency):
    def __init__(self, money):
        self.money = money

    def to_dollars(self):
        return round(self.money, 2)


