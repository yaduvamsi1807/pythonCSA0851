vcount = 0
ccount = 0
space_count = 0
line_count = 0

str_input = input("Enter the string: ")
str_input = str_input.lower()

for char in str_input:
    if char in ('a', 'e', 'i', 'o', 'u'):
        vcount += 1
    elif char >= 'a' and char <= 'z':
        ccount += 1
    elif char == ' ':
        space_count += 1
    elif char == '\n':
        line_count += 1

print("Total number of vowels:", vcount)
print("Total number of consonants:", ccount)
print("Total number of spaces:", space_count)
print("Total number of lines:", line_count)
