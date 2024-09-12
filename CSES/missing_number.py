n = int(input())
arr = list(map(int, input().split()))


su = (n * (n+1)) //2

for i in arr:
    su -= i

print(su)