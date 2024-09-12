def divide_numbers(n):
    total_sum = n * (n + 1) // 2

    # If the total sum is odd, it's not possible to divide into two equal sets
    if total_sum % 2 != 0:
        print("NO")
        return

    print("YES")
    
    # Target sum for each set
    target = total_sum // 2
    set1, set2 = [], []
    current_sum = 0
    
    # Fill set1 greedily from the largest number down to 1
    for i in range(n, 0, -1):
        if current_sum + i <= target:
            set1.append(i)
            current_sum += i
        else:
            set2.append(i)
    
    # Output the sets
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))

# Input
n = int(input())

# Function call
divide_numbers(n)
