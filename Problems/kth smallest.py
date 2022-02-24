
def kthsmallest(arr,k):
    arr.sort()
    return arr[k-1]


arr=[3,8,1,0,5,9]
k=6
print(kthsmallest(arr,k))
