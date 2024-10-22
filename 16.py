def is_prime(n, divisor=2):
    if n < 2:  
        return False
    elif n == divisor:  
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)
    
def find_primes_and_composites(start, end):
    primes = []
    composites = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return primes, composites

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers, composite_numbers = find_primes_and_composites(start, end)

print("Prime numbers in the range:")
print(prime_numbers)

print("Composite numbers in the range:")
print(composite_numbers)
