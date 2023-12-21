N=5

for i in range(N):
   # Inner loop for printing the alphabets from
   # A + N - 1 - i (i is row no.) to A + N - 1 (E in this case).
   for ch in range(ord('A') + N - 1 - i, ord('A') + N):
     print(chr(ch), end=" ")
   # Move to the next line.
   print()