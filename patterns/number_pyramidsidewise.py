n = 5
for i in range(1,n):
    #num
    for j in range(0,i):
        print(j+1,end="") 

    #space
    for k in range(1,2*(n-i)-1):
        print(" ",end="")

    #num
    for l in range(i,0,-1):
        print(l,end="")
    print()

        
# 1      1
# 12    21
# 123  321
# 12344321