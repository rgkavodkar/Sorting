__author__ = 'rg.kavodkar'

import random
import time

'''
Import all the necessary sorting algorithm files
'''
import insertion_sort
import merge_sort
import counting_sort
import quick_sort
import heap_sort
import bubble_sort
import selection_sort


'''
Set the random seed to some number so that the list is the same for all the cases
'''
random.seed(10)
random_list = random.sample(range(100000), 10000)
#
# # Bubble Sort
# start = time.time()
# bubble_sorted_list = bubble_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Bubble sort took", total_time, "seconds")
#
# random_list = random.sample(range(100000), 10000)
#
# # Insertion Sort
# start = time.time()
# insertion_sorted_list = insertion_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Insertion sort took", total_time, "seconds")
#
# random_list = random.sample(range(100000), 10000)
#
# # Selection Sort
# start = time.time()
# selection_sorted_list = selection_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Selection sort took", total_time, "seconds")
#
# random_list = random.sample(range(100000), 10000)
#
# # Quick Sort
# start = time.time()
# quick_sorted_list = quick_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Quick sort took", total_time, "seconds")
#
# random_list = random.sample(range(100000), 10000)
#
# # Merge Sort
# start = time.time()
# merge_sorted_list = merge_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Merge sort took", total_time, "seconds")
#
# random_list = random.sample(range(100000), 10000)
#
# Heap Sort
start = time.time()
heap_sorted_list = heap_sort.sort(random_list)
print(heap_sorted_list)
end = time.time()
total_time = (end - start)
print("Heap sort took", total_time, "seconds")

# random_list = random.sample(range(100000), 10000)
#
# # Counting Sort
# start = time.time()
# counting_sorted_list = counting_sort.sort(random_list)
# end = time.time()
# total_time = (end - start)
# print("Counting sort took", total_time, "seconds")


