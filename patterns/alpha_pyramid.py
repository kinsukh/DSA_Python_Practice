n = 5

# for i in range(1, n+1):
#     for j in range(1, n + i):
#         if n - i < j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

for i in range(0,n):
    #space 
    for j in range(0,n-i-1):
        print(" ",end="")

    #alpha character
    char = chr(65)
    for j in range(0,2*i+1):
        print(char,end = "")
        if j < int((2*i+1)/2):
            char = chr(ord(char)+1)
        else:
            char = chr(ord(char)-1)
        

    #space
    for j in range(0,n-i-1):
        print(" ",end="")
    
    print()

#     A    
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA