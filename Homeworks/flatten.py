def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)