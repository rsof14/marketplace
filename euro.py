from currency import Currency

EU = 1.2


class Euro(Currency):
    def __init__(self, money):
        self.money = money

    def to_dollars(self):
        return round(self.money * EU, 2)

