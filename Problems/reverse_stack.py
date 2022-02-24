r=[]
def reverse_stack(arr,n):
    if n<0:
        return
    r.append(arr[n])
    return reverse_stack(arr,n-1)

arr=[1,2,3]
n=len(arr)
reverse_stack(arr,n-1)
print(r)  