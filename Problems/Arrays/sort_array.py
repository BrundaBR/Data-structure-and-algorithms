#Recurrsive function
def helper():
  pass
#Main Function
def function(a):
    count0=0
    count1=0
    count2=0
    result=[]
    for i in range(len(a)):
        if a[i]==0:
            count0+=1
        elif a[i]==1:
            count1+=1
        elif a[i]==2:
            count2+=1
    for i in range(count0):
        result.append(0)
    for i in range(count1):
        result.append(1)
    for i in range(count2):
        result.append(2)

    return result
    

if __name__=='__main__':
  '''
  Obtain user input
  lis=[]
  n=int(input())
  for i in range(n):
    x=input()
    lis.append(x)
  '''
  arr=[0,2,1,2,0]
  #matrix=[[1,2,3][4,5,6][7,8,9]]
  print(function(arr))