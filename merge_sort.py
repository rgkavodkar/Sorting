__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    Split the list recursively until it reach unit size and retract from that point by merging the
    already sorted unit list, and so on.
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''

    # In the recursive calls, if the size of the list is 1, return it
    if len(list_) == 1:
        return list_

    # Find the mid point of the list for splitting
    mid_point = int(len(list_)/2)

    # The left and right halves of the list
    l_half = sort(list_[0: mid_point])
    r_half = sort(list_[mid_point:])

    # Merge the two sorted lists
    sorted_list = merge(l_half, r_half)
    return sorted_list


def merge(list_1, list_2):
    '''
    Given two sorted list, merge them to form a unified sorted list
    :param list_1: Sorted list 1
    :param list_2: Sorted list 2
    :return: Returns the merged sorted list
    '''

    # an empty list to construct the sorted list
    # 2 moving pointers for the 2 lists
    merged_list = list()
    l = 0
    r = 0

    # Starting from the head of both of the lists, add the smaller value to the sorted list
    # and move the corresponding pointer. Repeat until either of the pointers move out of scope
    while l < len(list_1) and r < len(list_2):
        if list_1[l] < list_2[r]:
            merged_list.append(list_1[l])
            l += 1
        else:
            merged_list.append(list_2[r])
            r += 1

    # For the pointer that dint move till the end, add the rest of the values in that list
    # to the sorted list
    if l < len(list_1):
        while l < len(list_1):
            merged_list.append(list_1[l])
            l += 1
    elif r < len(list_2):
        while r < len(list_2):
            merged_list.append(list_2[r])
            r += 1
    return merged_list

