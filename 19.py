def sort_names(names, order):
    """
    Sorts a list of names in ascending or descending order.

    Args:
    names (list): List of names to be sorted.
    order (str): 'asc' for ascending order, 'desc' for descending order.

    Returns:
    list: Sorted list of names.
    """
    if order == 'asc':
        return sorted(names)
    elif order == 'desc':
        return sorted(names, reverse=True)
    else:
        print("Invalid order specified. Please choose 'asc' for ascending or 'desc' for descending.")
        return []


def main():
    # Get input from the user
    names = input("Enter names separated by commas: ").split(',')
    order = input("Enter 'asc' for ascending order or 'desc' for descending order: ").strip().lower()

    # Sort names
    sorted_names = sort_names(names, order)

    # Print the sorted names
    if sorted_names:
        print("Sorted names:")
        for name in sorted_names:
            print(name.strip())


if __name__ == "__main__":
    main()
