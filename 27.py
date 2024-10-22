def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = (income - 150000) * 0.1
    elif income <= 500000:
        tax = 15000 + (income - 300000) * 0.2
    else:
        tax = 45000 + (income - 500000) * 0.3

    return tax

def main():
    income = float(input("Enter the income: "))

    if income < 0:
        print("Invalid input. Income cannot be negative.")
    else:
        tax = calculate_tax(income)
        print("Tax =", tax)

if __name__ == "__main__":
    main()
