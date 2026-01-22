from Security import Security

class Bond(Security):
    # Bond = אג"ח 
    def __init__(self, name, price, risk_level, interest_rate):
        super().__init__(name, price, risk_level)
        self.interest_rate = interest_rate

    def yearly_interest(self):
        return self.price * self.interest_rate