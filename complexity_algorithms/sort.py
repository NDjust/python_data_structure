from random import randint
import time


def bubble_sort(L):
    '''
    insert sort algorithms 

    best case : O(n)
    worst case : O(n2)
    '''
    for i in range(len(L) -1):
        for j in range(len(L)):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    return L
   
   
def merge_sort(L):
    '''
    merge sort algorithms

    time complexity : O(nlogn)
    '''
    if len(L) < 2:
        return L

    mid = len(L) // 2
    low_L = merge_sort(L[:mid])
    high_L = merge_sort(L[mid:])

    merged_L = []
    l = h = 0
    while l < len(low_L) and h < len(high_L):
        if low_L[l] < high_L[h]:
            merged_L.append(low_L[l])
            l += 1
        else:
            merged_L.append(high_L[h])
            h += 1
    merged_L += low_L[l:]
    merged_L += high_L[h:]
    return merged_L

# test_case = [54, 26, 93, 22, 11, 55, 44]

# print(insert_sort(test_case))

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    num_list = [randint(0, num) for i in range(num)] # create Random test case.
    start_time = time.time()
    result = insert_sort(num_list)
    print("insert sort algorithms time: {}".format(time.time() -start_time))
    start_time = time.time()
    result = merge_sort(num_list)
    print("merge sort algorithms time: {}".format(time.time() -start_time))
    