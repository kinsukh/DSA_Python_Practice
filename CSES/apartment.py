n,m,k = map(int,input().split())
desired_size = list(map(int,input().split()))
appartment_size = list(map(int,input().split()))

desired_size.sort()
appartment_size.sort()
i,j = 0, 0
c = 0
n = len(desired_size)
m = len(appartment_size)

while i < n and j < m:
    if abs(desired_size[i] - appartment_size[j]) <= k:
        c += 1
        i += 1
        j += 1
    elif desired_size[i] < appartment_size[j]:
        i += 1
    else:
        j += 1

print(c)


