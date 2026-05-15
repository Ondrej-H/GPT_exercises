def make_list_without_even(lst):
    result_list = []
    for element in lst:
        if element % 2 != 0:
            result_list.append(element)
    return result_list


list1 = [2, 4, 5, 6, 8, 9]
print(make_list_without_even(list1))