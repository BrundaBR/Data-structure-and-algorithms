def binary_search(a,t):
    # #find k rotations
    # k=0
    # for i in range(len(a)):
    #     if a[i+1] < len(a) and a[i]  > a[i+1]:
    #         x=a[i+1:]
    #         k=len(x)
    #         break
    # a.sort()
    # #binary search
    # start=0
    # end=len(a)-1
    # while start<=end:
    #     mid=start+(end-start)//2
    #     if a[mid]==target:
    #         #return mid+k
    #         if mid==0:
    #             return mid+k+1
            
            
    #     elif a[mid] > target:
    #         end=mid-1
    #     elif a[mid] < target:
    #         start=mid+1
    # return -1
arr=[4,5,6,7,0,1,2]
target=0
print(binary_search(arr,target))