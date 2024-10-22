def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def non_prime_numbers(A, B):
    non_prime_list = []
    for num in range(A, B + 1):
        if not is_prime(num):
            non_prime_list.append(num)
    return non_prime_list

if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B:  "))
    
    non_primes = non_prime_numbers(A, B)
    print("Non-Prime numbers between", A, "and", B, "are:", ', '.join(map(str, non_primes)))
