def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

try:
    decimal_number = int(input("Decimal Number: "))
    if decimal_number < 0:
        raise ValueError("Decimal number cannot be negative.")

    binary_number = decimal_to_binary(decimal_number)
    octal_number = decimal_to_octal(decimal_number)

    print("Binary Number =", binary_number)
    print("Octal =", octal_number)
except ValueError as ve:
    print("Error:", ve)
