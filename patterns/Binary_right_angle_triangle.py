n=5
c=1
for i in range(n):
    for j in range(i):
        if c%2==0 :
            print(0,end='')
        else:
            print(1,end="")
        # print(str(c)+"cvalue")
        c+=1
        # print(str(c)+"cvalue")
    print()

# 1
# 01
# 010
# 1010