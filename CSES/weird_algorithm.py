n = int(input())

def recur(n):
    if n%2 == 0:
        print(n, end=" ")
        recur(n//2)
    elif n == 1:
        if n == 1:
            print(n, end=" ")
            return
    else:
        print(n, end=" ")
        recur(n*3+1)
    
recur(n)