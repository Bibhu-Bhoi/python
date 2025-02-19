'''def copy_set_one_element_at_a_time(input_set):
    new_set = set()
    for element in input_set:
        new_set.add(element)
    return new_set

# Input set
input_set = eval(input("Enter the set (in the format {element1, element2, ...}): "))

# Copy set one element at a time
new_set = copy_set_one_element_at_a_time(input_set)

# Print the new set
print("New set after copying one element at a time:")
print(new_set)
'''
'''def set_operations(set1, set2):
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("\nSet Operations:")
    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference (Set 1 - Set 2):", set1.difference(set2))
    print("Difference (Set 2 - Set 1):", set2.difference(set1))
    print("Symmetric Difference:", set1.symmetric_difference(set2))

# Input sets
set1 = eval(input("Enter the first set (in the format {element1, element2, ...}): "))
set2 = eval(input("Enter the second set (in the format {element1, element2, ...}): "))

# Perform set operations
set_operations(set1, set2)
'''
def combine_and_remove_duplicates(set1, set2):
    combined_set = set1.union(set2)
    return combined_set

# Input sets
set1 = set(input("Enter the first set (separated by spaces): ").split())
set2 = set(input("Enter the second set (separated by spaces): ").split())

# Combine sets and remove duplicates
new_set = combine_and_remove_duplicates(set1, set2)

# Print the new set
print("New set after combining and removing duplicates:", new_set)
