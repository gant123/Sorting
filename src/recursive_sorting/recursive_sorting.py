# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):

    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    x, y = 0, 0
    for i in range(elements):
        if len(arrA) == x:
            for j in range(y, len(arrB)):
                merged_arr[i + j - y] = arrB[j]
            return merged_arr
        elif len(arrB) == y:
            for j in range(x, len(arrA)):
                merged_arr[i + j - x] = arrA[j]
            return merged_arr

        if arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    split = len(arr) // 2
    return merge(merge_sort(arr[:split]), merge_sort(arr[split:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return arr

    while start <= mid and start2 <= end:

        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
      if l < r:

        m = l + (r - l) / 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
