# s = input()
# tom = input()

# print(s.count(tom))


##      or      ##

s = input()
tom = input()
c = 0
i = 0
le = len(tom)
while i < len(s):
    if s[i:i+le] == tom:
        c+=1
    i+=1

print(c)