n = 6 
for i in range(n-1,0,-1):
    #num
    for j in range(0,i):
        print('*',end="") 

    #space
    for k in range(1,2*(n-i)-1):
        print(" ",end="")

    #num
    for l in range(i,0,-1):
        print("*",end="")
    print()

for i in range(1,n):
    #num
    for j in range(0,i):
        print('*',end="") 

    #space
    for k in range(1,2*(n-i)-1):
        print(" ",end="")

    #num
    for l in range(i,0,-1):
        print("*",end="")
    print()

        

