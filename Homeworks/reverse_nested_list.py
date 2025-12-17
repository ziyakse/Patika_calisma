def reverse_nested_list(n_list):
    reversed_top = n_list[::-1]

    new_list = [reverse_nested_list(item) if isinstance(item, list) else item for item in reversed_top]
    
    return new_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_nested_list(input_list)