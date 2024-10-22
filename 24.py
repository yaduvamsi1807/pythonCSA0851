def main():
    positive_numbers = []
    negative_numbers = []
    
    while True:
        num = int(input("Enter a number (-1 to stop): "))
        
        if num == -1:
            break
        
        if num >= 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)
    
    if positive_numbers:
        avg_positive = sum(positive_numbers) / len(positive_numbers)
        print("Average of positive numbers:", avg_positive)
    else:
        print("No positive numbers were entered.")
    
    if negative_numbers:
        avg_negative = sum(negative_numbers) / len(negative_numbers)
        print("Average of negative numbers:", avg_negative)
    else:
        print("No negative numbers were entered.")

if __name__ == "__main__":
    main()
