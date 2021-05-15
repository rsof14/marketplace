from currency import Currency


class Product:
    def __init__(self, name: str, pr: Currency, num: int):
        self.name = name
        self.price = pr
        self.price = self.price.to_dollars()
        self.num = num



