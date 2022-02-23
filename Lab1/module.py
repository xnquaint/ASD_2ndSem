from random import randint


def createArray():
    array = []
    num = int(input("Enter number of elements in array: "))
    key = input(
        "Enter 'a' to generate an average array,\n" + "'b' to generate the best,\n" + "'w' to generate the worst.\n")
    if key == 'a':
        array = [randint(0, num) for i in range(num)]
    elif key == 'w':
        array = [num - 1 - i for i in range(num)]
    elif key == 'b':
        array = [i for i in range(num)]
    return array


def bubbleSort(array):
    n = len(array)
    comps = 0
    swaps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            comps += 1
            if array[i] > array[i + 1]:
                swaps += 1
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return comps, swaps


def combSort(array):
    size = len(array)
    gap = size
    shrink = 1.3
    is_sorted = False
    comps = 0
    swaps = 0
    while not is_sorted:
        gap = int(gap//shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        for i in range(size - gap):
            comps += 1
            if array[i] > array[i+gap]:
                swaps += 1
                array[i], array[i+gap] = array[i+gap], array[i]
                is_sorted = False
    return comps, swaps

