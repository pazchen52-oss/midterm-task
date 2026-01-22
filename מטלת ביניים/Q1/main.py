from invoice import Invoice

def main():
    num = input("Invoice number: ")
    cust = input("Customer name: ")
    amt = float(input("Amount: "))
    tax = float(input("Tax rate between 0 to 1: "))
    desc = input("Description: ")

    invoice = Invoice(num, cust, amt, tax, desc)


    print(f"Total with tax: {invoice.total_with_tax():.2f} ")
    invoice.show()


if __name__ == "__main__":
    main()