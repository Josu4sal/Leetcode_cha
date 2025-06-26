arr = [9, 9, 9, 9, 9, 9, 8, 9, 9]


def sumar1(arr):
    n=len(arr)
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 9:
            arr[i]+=1
            return arr
        arr[i]=0
    return [1]+[0]*n

print(sumar1(arr=arr))


