class Security:
#Security= נייר ערך
    def __init__(self, name, price, risk_level): 
        self.name = name
        self.price = price
        self.risk_level = risk_level

    def info(self):
        return f"{self.name} | Price: {self.price} | Risk: {self.risk_level}"