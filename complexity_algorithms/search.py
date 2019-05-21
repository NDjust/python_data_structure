from random import randint
import time

def linear_search(L, x):
    '''
    using linear search algorithms 
    time complexity 
    -> O(n)

    parmas:
    L: list
    x: target num
    '''
    for i in range(len(L)):
        if x == L[i]:
            return i
    return -1


def binary_search(L, x):
    '''
    using binary search algorithms 
    
    time complexity 
    -> O(log n)

    parmas:
    L: list
    x: target num
    '''
    lower = 0
    upper = len(L) - 1
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        if L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
    return idx


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    target = int(input("Enter the number of targets: "))
    num_list = sorted([randint(0, num) for i in range(num)]) # create Random numbers list.
    target_list = [randint(0, num) for i in range(target)] # create Random target num list.
    start_time = time.time()
    result = [binary_search(num_list, target) for target in target_list]
    print("Binary search found target number time: {}".format(time.time() -start_time))
    start_time = time.time()
    result = [linear_search(num_list, target) for target in target_list]
    print("linear search found target number time: {}".format(time.time() -start_time))