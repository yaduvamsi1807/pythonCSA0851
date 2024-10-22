def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
lcm = find_lcm(num1, num2)

print("The GCD of", num1, "and", num2, "is", gcd)
print("The LCM of", num1, "and", num2, "is", lcm)
