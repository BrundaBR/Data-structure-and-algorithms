#Recurrsive function
def helper():
  pass
#Main Function
def function(a):
    res_max=a[0]
    res_min=a[0]
    n=len(a)
    #step1: handle edge n=1
    #step2: n>2
    #step3: compare each ele with max and min and update values
    #step4: return result
    if n>2:
        for i in range(n):
            if a[i] < res_min:
                res_min=a[i]
            elif a[i] >res_max:
                res_max=a[i]
            else:
                continue
    return res_max,res_min

 


if __name__=='__main__':
  '''
  Obtain user input
  lis=[]
  n=int(input())
  for i in range(n):
    x=input()
    lis.append(x)
  '''
  arr=[1]
  #matrix=[[1,2,3][4,5,6][7,8,9]]
  print(function(arr))