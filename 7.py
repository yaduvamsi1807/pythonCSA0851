def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    try:
        N = int(input("Enter the value of N: "))
        if N <= 0:
            print("N should be a positive integer.")
        else:
            fib_sequence = fibonacci(N)
            print("Fibonacci sequence up to the", N, "th number:", ' '.join(map(str, fib_sequence)))
    except ValueError:
        print("N should be a positive integer.")
