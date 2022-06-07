def merge(list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = list[l + i]

    for j in range(0, n2):
        R[j] = list[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1


def merge_Sort(list, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_Sort(list, l, m)
        merge_Sort(list, m + 1, r)
        merge(list, l, m, r)


list = [12, 11, 13, 5, 6, 7]
n = len(list)
print("Given array is")
for i in range(n):
    print("%d" % list[i], end=" ")

merge_Sort(list, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % list[i], end=" ")
