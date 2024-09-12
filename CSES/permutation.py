n = int(input())

if 1< n < 4:
    print("NO SOLUTION")
    exit()

lis = [i for i in range(1,n+1)]

new = []
i = 1
while len(new)!= n:
    # new.append(lis[i])
    if i  <= n-1:
        new.append(lis[i])
        i += 2
    else:
        i = 0

print(*new)
