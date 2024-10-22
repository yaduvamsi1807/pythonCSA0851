def reverse_word(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

if __name__ == "__main__":
    input_string = input("String: ")
    reversed_string = reverse_word(input_string)
    print("Reverse String:", reversed_string)

