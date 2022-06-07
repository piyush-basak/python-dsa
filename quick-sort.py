def partition(list, low, high):
    i = (low - 1)
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)


def quick_Sort(list, low, high):
    if len(list) == 1:
        return list
    if low < high:
        pi = partition(list, low, high)

        quick_Sort(list, low, pi - 1)
        quick_Sort(list, pi + 1, high)


list = [14, 33, 27, 35, 10]
n = len(list)
quick_Sort(list, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % list[i], end=" ")