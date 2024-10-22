def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(f"{j / 10:.1f}", end=" ")
        print()
rows = 4
print_pattern(rows)
