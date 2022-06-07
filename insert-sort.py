def insertion_Sort(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

list = [14, 33, 27, 35, 10]
insertion_Sort(list)
print('Sorted Array in Ascending Order:')
print(list)
