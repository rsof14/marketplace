from product import Product
from currency import Currency
from dollar import Dollar
from rubles import Rubles
from euro import Euro

convert = [1, 0.83, 76.9230769]  # чтобы перевести доллары в любую валюту (доллары, евро, рубли)
cur_name = ["dollars", "euro", "rubles"]


# prices in dollars
class Marketplace:
    def __init__(self):
        self.products = {"apple": Product("apple", Dollar(2), 10),
                         "avocado": Product("avocado", Euro(3), 10),
                         "dress": Product("dress", Rubles(2000), 5)}

    def show_products(self, currency):
        for product in self.products.values():
            print(
                f"{product.name} for {round(product.price * convert[currency - 1], 2)} {cur_name[currency - 1]}, {product.num} items left")

    def buy(self, item_name, item_num, money_to_buy):
        item = self.products[item_name]
        if item_num > item.num:
            print(
                f"At the moment, we do not have that amount of this product. You can purchase {item.num} units of this product")
        else:
            if item_num * item.price > money_to_buy:
                print("You don't have enough money to buy")
            else:
                print("You can buy")
                item.num -= item_num
                if item.num == 0:
                    del item

    def user(self):
        print("Hi! Please choose your currency: 1 - dollar, 2- euro, 3- ruble ")
        currency = int(input())
        action = 0
        while action != 4:
            print("""
            Press 1 to view the assortment of products
            Press 2 to choose products
            Press 3 to change currency
            Press 4 to finish """)
            action = int(input())
            if action == 1:
                self.show_products(currency)
            if action == 2:
                print("Enter the name and quantity of the product, how much money you have to buy")
                item_name = input()
                item_num = int(input())
                money_to_buy = round(int(input()) / convert[currency - 1], 2)
                self.buy(item_name, item_num, money_to_buy)
            if action == 3:
                print("Please choose your currency: 1 - dollar, 2- euro, 3- ruble ")
                currency = int(input())
        print("Goodbye!")


if __name__ == "__main__":
    Market = Marketplace()
    Market.user()
