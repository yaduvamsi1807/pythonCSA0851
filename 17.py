def print_numbers_with_skip(M, N, K):
    num = M
    while num <= N:
        print(num, end=", ")
        num += K  # Skip K numbers in each iteration
M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))
K = int(input("Enter the number of skips (K): "))
print("Numbers from", M, "to", N, "by skipping", K, "numbers in between:")
print_numbers_with_skip(M, N, K)
