__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    Iterates through the entire list in each of the iteration, choosing the smallert
    element and moving it to the head of the list. In each of the iteration i, it moves
    the ith smallest element to the position i. The next iteration will start from
    i + 1 onwards
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    for i in range(len(list_)):
        # Assume the first element is the smallest
        min_element = i
        for j in range(i + 1, len(list_)):
            # Upon encountering a smaller element, put that as the smallest index
            # By the end of the iteration, the smallest element's index will be in min_element
            if list_[j] < list_[min_element]:
                min_element = j
        list_[i], list_[min_element] = list_[min_element], list_[i]
    return list_