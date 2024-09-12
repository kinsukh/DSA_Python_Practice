n = int(input())
for i in range(n):
    x,y = map(int,input().split())

    if x>y:
        ans = (x-1)*(x-1)
        if x%2 == 0:
            print(ans + 2*x-y)
        else:
            print(ans + y)
    else:
        ans = (y-1)*(y-1)
        if y%2 == 0:
            print(ans+x)
        else:
            print(ans + 2*y-x)