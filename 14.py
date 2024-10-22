def remove_duplicates_sorted_array(arr):
    unique_elements = sorted(set(arr))
    return unique_elements

input_array = input("Enter the array elements separated by space: ")

output_array = remove_duplicates_sorted_array(input_array)
print("Sorted Array without Duplicates:", output_array)

#2.which are duplicated value

# Taking user input for the array
user_input = input("Enter the array elements separated by space: ")
arr = list(map(int, user_input.split()))

print("Duplicate elements in given array: ")
# Searches for duplicate element
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[j])
