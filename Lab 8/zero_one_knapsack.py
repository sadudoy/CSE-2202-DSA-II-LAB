

def zero_one_knapsack(p, w, capacity):
    n = len(w)
    dp = [[0] * (capacity+1)] * (n+1)

    for i in range (1, n+1):
        for j in range (1, capacity+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i-1]]+p[i-1])
    return dp[n][capacity]


p = [1, 2, 5, 6]
w = [2, 3, 4, 7]
capacity = 8

print(zero_one_knapsack(p, w, capacity))