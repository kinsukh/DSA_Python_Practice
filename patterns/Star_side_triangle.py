# Approach 1
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(n,1,-1):
#     for j in range(i-1):
#         print("*",end="")
#     print()

# Approach 2
n = 5
for i in range(1,(2*n-1)+1):
    if i<=n:
        for j in range(i):
            print("*",end="")
        print()
    else:
        for j in range(2*n-i):
            print("*",end="")
        print()
    
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *