def is_multiple(a, b):
    """Return True if one number is a multiple of the other."""
    if b == 0 or a == 0:
        return False
    return a % b == 0 or b % a == 0


def main():
    while True:
        num1 = float(input("Enter first number (-1 to stop): "))
        if num1 == -1:
            break

        num2 = float(input("Enter second number (-1 to stop): "))
        if num2 == -1:
            break

        if is_multiple(num1, num2):
            print("One number is a multiple of the other.")
        else:
            print("They are NOT multiples of each other.")

    print("Program ended.")


if __name__ == "__main__":
    main()