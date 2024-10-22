def find_maximum(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        return max(a, b, c)
    except ValueError:
        return "Input must be numeric."

if __name__ == "__main__":
    try:
        nums = input("Enter three numbers separated by spaces: ").split()
        if len(nums) != 3:
            print("Please enter exactly three numbers.")
        else:
            max_num = find_maximum(*nums)
            print("Maximum number:", max_num)
    except Exception as e:
        print("An error occurred:", e)
