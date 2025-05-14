# Write a function called filter_even_numbers that takes a list of integers and returns a new list containing only the even numbers.

def filter_even_numbers(num):
    return [i for i in num if i%2==0]

# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []

#---------------------------------------------------------------------------------------------------------------------
#Write a function called merge_sorted_lists that takes two sorted lists and returns a new sorted list containing all elements from both lists.

def merge_sorted_lists(lis1,lis2):
    return sorted(lis1 + lis2)

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]


