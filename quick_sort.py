__author__ = 'rg.kavodkar'


def sort(list_):
    '''
    Performs the sorting recursively. Chooses the pivot element (last element in the list) and
    moves it its right position in the list. The elements to its left will all be smaller in
    value and the elements to the right will all be higher in value
    :param list_: a list of numbers for sorting
    :return: the sorted list
    '''
    length = len(list_)
    quick_sort(list_, 0, length - 1)
    return list_


def quick_sort(list_, left, right):
    '''
    Since the sorting is performed inplace, the left and right indices of the sublists are passes
    :param list_: The entire to be sorted
    :param left: The left index of the sublist, ie, the start index
    :param right: The right index of the sublist, ie, the end index
    :return: A sorted sublist
    '''

    # check if the list size is atleast 1
    if left < right:
        # Perform the partion and palce the pivot element in its right position
        partition = create_partition(list_, left, right)

        # Recursively perform the sort on the left and the right sublists
        quick_sort(list_, left, partition - 1)
        quick_sort(list_, partition + 1, right)


def create_partition(list_, left, right):
    '''
    Find the index of the actual position of the pivot element
    :param list_: The entire list
    :param left: The left index of the sublist, ie, the start index
    :param right: The right index of the sublist, ie, the end index
    :return: Correct position of the pivot
    '''

    # Take the right-most element in the list as the pivoy
    pivot = list_[right]
    # Initialize the correct position of the list to be one less than the start index
    i = left - 1
    for j in range(left, right):
        # Whenever there is an element lesser than the pivot, increment i and swap the
        # jth element with the ith.
        if list_[j] < pivot:
            i += 1
            list_[i], list_[j] = list_[j], list_[i]
    # P osition i is the index that is one less than the correct position of the pivot
    # Swap the pivot with i + 1
    list_[i + 1], list_[right] = list_[right], list_[i + 1]
    return i + 1