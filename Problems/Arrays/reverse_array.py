
'''
O(n) time complexity and O(1) space complexity

'''

def arrayReverse(a):
    i=0
    j=len(a)-1
    while i < j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return a
arr=[1,2,3,4,5]
print(arrayReverse(arr))