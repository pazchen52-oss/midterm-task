class Invoice:
    def __init__(self, number, customer, amount, tax_rate, description):
        self.number = number
        self.customer = customer
        self.description = description
        self.tax_rate = tax_rate
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = value

    def total_with_tax(self):
        return self.amount * (1 + self.tax_rate)

    def show(self):
        print(f"Invoice {self.number} for {self.customer}: {self.total_with_tax():.2f} total")



