def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            # shift left until correct position found
            arr[j] = arr[j - 1]
            j -= 1
        # insert at correct position
        arr[j] = temp

    return arr


# implement the Bubble Sort function below
def bubble_sort(arr):
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swaps_occurred = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    if maximum == -1:
        maximum = max(arr)

    # count the number of each element in original arr
    count = [0] * (maximum+1)
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[value] += 1

    # reinsert values into original array using counts
    j = 0
    for i in range(0, len(count)):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    # return sorted array
    return arr
