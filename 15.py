def count_special_characters(statement):
    special_characters = "~`!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    count = 0
    for char in statement:
        if char in special_characters:
            count += 1
    return count

# Example usage:
statement = input("Enter a statement: ")
special_count = count_special_characters(statement)
print("Number of special characters:", special_count)
