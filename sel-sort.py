def selection_Sort(list, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if list[i] < list[min_idx]:
                min_idx = i
        (list[step],list[min_idx]) = (list[min_idx], list[step])


list = [14, 27, 33, 35, 10]
size = len(list)
selection_Sort(list, size)
print('Sorted Array in Ascending Order:')
print(list)
