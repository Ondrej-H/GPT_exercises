def remove_even(lst):
    for element_index in range(len(lst) - 1, -1, -1):
        if lst[element_index] % 2 == 0:
            lst.pop(element_index)
    return lst


list1 = [2, 4, 5, 6, 8, 9]
print(remove_even(list1))