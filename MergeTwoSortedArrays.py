#Below is the code to merge two sorted Arrays.
def merge(self, arr1, m, arr2, n):
    i, j = 0, 0
    arr3 = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    
    if i < m:
        for k in range(i, m):
            arr3.append(arr1[k])
    else:
        for k in range(j, n):
            arr3.append(arr2[k])
    
    arr1.clear()
    arr1.extend(arr3)
