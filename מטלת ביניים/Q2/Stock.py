from Security import Security

class Stock(Security):
    #Stock = מניה
    def __init__(self, name, price, risk_level, profit_rate):
        super().__init__(name, price, risk_level)
        self.profit_rate = profit_rate
    def calculate_dividend(self):
        return self.price * self.profit_rate