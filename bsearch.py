# TODO: Binary Search # regular loop results in linear-time complexity
def binary_search(list, item, begin_index, end_index):
    if end_index >= begin_index:
        mid = begin_index + (end_index - begin_index) // 2

        if list[mid] == item:
            return mid

        elif list[mid] > item:
            return binary_search(list, item, begin_index, mid - 1)

        else:
            return binary_search(list, item, mid + 1, end_index)

    else:
        return -1


list = [3, 4, 5, 6, 7, 8, 9]
item = 5

result = binary_search(list, item, 0, len(list) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
