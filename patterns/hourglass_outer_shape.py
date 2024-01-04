n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(n,1,-1):
#     for j in range(i-1):
#         print("*",end="")
#     print()
    
insp = 2*n - 2
for i in range(1,(2*n-1)+1):
    stars = i
    if (i>n):
        stars = 2*n-i
    # //stars
    for j in range(0,stars):
        print("*",end = '')
    # //spaces
    for j in range(0,insp):
        print(" ",end = '')
    # //stars
    for j in range(0,stars):
        print("*",end = '')
    print()
    if (i<n):
        insp -=2
    else:
        insp +=2


# output
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *