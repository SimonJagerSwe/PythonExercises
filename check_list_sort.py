########## CHECK IF A LIST IS SORTED ##########

# MY SOLUTION
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [1, 2, 4, 3, 10, 8, 9, 7, 6, 5]
# print(first_list)
# print(second_list)

def check_list_sort():
    sorted_first = sorted(first_list)
    # print(sorted_first)
    sorted_second = sorted(second_list)
    # print(sorted_second)
    if first_list == sorted_first:
        print('First list is sorted!')
    else:
        print('First list is not sorted!')
    if second_list == sorted_second:
        print('Second list is sorted!')
    else:
        print('Second list is not sorted!')

check_list_sort()

# SUGGESTED SOLUTION
'''
def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            asc = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            desc = False
    return asc or desc

is_sorted(lst)
'''