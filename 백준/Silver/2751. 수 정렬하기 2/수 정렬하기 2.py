import sys
from typing import MutableSequence

N = int(sys.stdin.readline())

unsorted_list = []
sorted_list = []

def slice_list(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left_list = list[:mid]
    right_list = list[mid:]
    left_list = slice_list(left_list)
    right_list = slice_list(right_list)
    return merge_sort(left_list, right_list)

def merge_sort(left, right):
    merged_list = []
    l=h=0

    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[h])
            h += 1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list


for i in range(N):
    unsorted_list.append(int(sys.stdin.readline()))

sorted_list = slice_list(unsorted_list)

for i in sorted_list:
    print(i)