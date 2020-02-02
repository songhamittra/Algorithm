def insertion_sort(A):
    length = len(A)

    for j in range(1, length):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    print(A)




def selection_sort(A):
    length = len(A)

    for i in range(0, length-1,1):
        min=i
        for j in range(i+1,length,1) :
            if A[j]<A[min] :
                min=j

        if min!=i :
            A[i],A[min]=A[min],A[i]
    print(A)




def bubble_sort(A):
    length = len(A)

    for i in range(0, length,1):
        for j in range(0,length-i-1,1) :
            if A[j]>A[j+1] :
                A[j],A[j+1]=A[j+1],A[j]
    print(A)


def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1




def counting_sort(array1, k):
    m = k + 1
    count = [0] * m

    for a in array1:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1
    return array1

A = [12, 1, 23, 4, 34, 11, 49]
insertion_sort(A)
selection_sort(A)
bubble_sort(A)
mergeSort(A)
print(A)
print(counting_sort(A, 49))