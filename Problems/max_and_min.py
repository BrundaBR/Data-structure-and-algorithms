def min_and_max(arr):
    minimum=1000
    maximum=0
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum=arr[i]
        elif arr[i] > maximum:
            maximum=arr[i]
    
    print(maximum,minimum)
    
arr=[1,2,3,4,5,6,7,8]
min_and_max(arr)