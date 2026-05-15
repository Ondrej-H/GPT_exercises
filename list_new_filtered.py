def filter_greater(lst, threshold):
    new_lst = []
    for element in lst:
        if element > threshold:
            new_lst.append(element)
    return new_lst


print(filter_greater([1, 5, 3, 7], 3))