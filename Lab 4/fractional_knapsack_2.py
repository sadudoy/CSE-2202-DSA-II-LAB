# fractional knapsack without class

arr = [(100, 20), (60, 10), (100, 50), (200, 50)]

arr.sort(key = lambda x : x[0] / x[1], reverse=True)
t_profit = current_weight = 0
w = 90

for i in range(0, len(arr)):
    if current_weight+arr[i][1] <= w:
        current_weight += arr[i][1]
        t_profit += arr[i][0]

    else:
        remaining = w - current_weight
        cost = (arr[i][0] / arr[i][1]) * remaining
        t_profit += cost

print(t_profit)