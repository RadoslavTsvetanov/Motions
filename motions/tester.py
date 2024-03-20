def check_keys_appear(set1, set2):
    # Iterate through each element in set1
    for element in set1:
        # If any element from set1 is not in set2, return False
        if element not in set2:
            return False
    # If all elements from set1 are found in set2, return True
    return True

# Example usage:
listening_keys = set({'a', 'b'})
current_keys = set({'b', 'a'})

print(check_keys_appear( current_keys,listening_keys))