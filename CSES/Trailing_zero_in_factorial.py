n = int(input())

# def fact(n):
#     cn = 1

#     for i in range(n,0,-1):
#         cn = cn * i
    
#     return cn

def trailing_zero(n):
    # c = 0
    # s = str(fact(n))
    # for i in range(len(s)-1,-1,-1):
    #     if s[i] == '0':
    #         c += 1
    #     else:
    #         break
    # return c
    if n == 0:
        return 0
    return n // 5 + trailing_zero(n // 5)

print(trailing_zero(n))
