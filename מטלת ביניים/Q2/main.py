from Stock import Stock
from Bond import Bond
from Option import Option

def main():
    stock = Stock("Apple", 180, "Medium", 0.02)
    bond = Bond("US Treasury", 1000, "Low", 0.05)
    option = Option("Apple Call", 12, "High", 10)

    print(stock.info())
    print("Dividend:", stock.calculate_dividend())

    print(bond.info())
    print("Yearly interest:", bond.yearly_interest())

    print(option.info())
    print("Profitable:", option.is_profitable())

if __name__ == "__main__":
    main()