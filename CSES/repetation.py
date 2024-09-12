s = input()
max = 1
count = 1   
if len(set(s)) == 1:
    print(len(s))
    exit()
elif len(s) == 1:
    print(1)
    exit()
for i in range(len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        count = 1
    if count > max:
        max = count

print(max)