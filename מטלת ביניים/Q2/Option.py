from Security import Security

class Option(Security):
    #Option = אופציות
    def __init__(self, name, price, risk_level, sell_price):
        super().__init__(name, price, risk_level)
        self.sell_price = sell_price

    def is_profitable(self):
        return self.price > self.sell_price