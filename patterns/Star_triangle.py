
n = 5

for i in range(1, n+1):
    for j in range(1, n + i):
        if n - i < j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#     *
#    ***
#   *****
#  *******
# *********