n,x  = map(int,input().split())
childs_weight = list(map(int,input().split()))
childs_weight.sort()
i = 0
j = n-1
c = 0
while i <= j:
    if childs_weight[i] + childs_weight[j] <= x:
        c += 1
        i += 1
        j -= 1
    elif childs_weight[j] <= x:
        j -= 1
        c += 1

print(c)