from module import *

array = createArray()
comparisons = 0
swaps = 0
print(f"Generated array: {array}")
mode = input("Enter 'b' if you want to use bubble sort\n"+"Enter 'c' if you want to use comb sort\n")
if mode == 'b':
    comparisons, swaps = bubbleSort(array)
elif mode == 'c':
    comparisons, swaps = combSort(array)
print(f"Sorted array: {array}")
print(f"Number of comparisons: {comparisons}\n" + f"Number of swaps: {swaps}")
