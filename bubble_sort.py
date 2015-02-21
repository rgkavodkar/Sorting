__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    This implementation is the 'sinking sort'. The largest/heaviest numbers are put to the
    bottom of the list in subsequent iterations. For the actual bubble sort, the
    smallest/lightest element should rise to the top in consecutive iterations
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    length = len(list_)
    while length > 0:
        # optimized_len is used to cut short the iterations since the largest elements are
        # put to the last of the list in the right order, through the iterations
        # Once the elements are in the right position (starting from the last), there is
        # no need to check against those
        optimized_len = 0

        # iterate through the list
        for i in range(1, length):
            # compare two consecutive elements. Swap such that the higher valued elements
            # is to the right
            if list_[i - 1] > list_[i]:
                list_[i - 1], list_[i] = list_[i], list_[i - 1]
                optimized_len = i
        # optimized_len will contain the last swapped position. Because of the nature of
        # bubble sort, the elements after the swapped positions are sorted and in their
        # right place. Therefore, update the length to which the next iteration should
        # be run
        length = optimized_len

    # return the sorted list
    return list_