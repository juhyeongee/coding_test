def merge(list1, list2):
    result = []
    while len(list1)+len(list2) !=  0:
        if len(list1) == 0:
            result.append(list2.pop(0))
        elif len(list2) == 0:
            result.append(list1.pop(0))
        elif list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    return result

def merge_sort(my_list):
    half = len(my_list)//2
    first_half = my_list[:half]
    second_half = my_list[half:]
    first_half = sorted(first_half)
    second_half =  sorted(second_half)

    return merge(first_half, second_half)

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7,10, 11, 4, 15, 13, 1, 6, 4]))
