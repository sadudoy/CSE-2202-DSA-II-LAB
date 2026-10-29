prev1 = 0
prev2 = 1
current = prev1 + prev2

n = 8

for i in range(2, n):
    prev1 = prev2
    prev2 = current
    current = prev1+prev2

print(current)


