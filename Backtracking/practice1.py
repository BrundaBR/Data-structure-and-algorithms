def fun1(x,y):
    if x==0:
        return y
    else:
        print(y)
        return fun1(x-1,y+x)

def main():
    print(fun1(3,3))
main()