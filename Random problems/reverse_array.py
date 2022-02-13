new_string=""
def reversestr(s,n):
    print(n)
    if n<0:
        return
    #subproblem
    print(s[n])
    return reversestr(s,n-1)
    
def main():
    s="Geek"
    print(reversestr(s,len(s)-1))

main()


# def reverse(s):
#     new_s=""
#     for i in range(len(s)-1,-1,-1):
#         new_s+=s[i]
#     return new_s
        


# s="Geeks"
# print(reverse(s))