def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


list = [14, 33, 27, 35, 10]

bubble_sort(list)

print("Sorted List in Ascending Order:", list)
