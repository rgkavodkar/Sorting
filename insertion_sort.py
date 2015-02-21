__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    Pick the ith node in each iteration and pull them to front of the list until it meets a node that is lesser than itself
    The nodes further than the ith node in the ith iteration are not touch until i reaches that value
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    for i in range(1, len(list_)):
        # Choose the ith node as the key
        key = list_[i]
        j = i - 1

        # Compare the key backwards (which is a sorted list) and put the key in its right position
        while j >= 0 and list_[j] > key:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
    return list_