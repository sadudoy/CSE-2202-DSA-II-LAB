# Fractional Knapsack Without Class

def fractional_knapsack(value, weight, capacity):

    # Store each item
    arr = []
    for i in range(len(value)):
        arr.append((value[i], weight[i]))

    # Sort 
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)

    t_profit = 0.0
    current_weight = 0

    # Select items
    for i in range(len(arr)):

        if current_weight + arr[i][1] <= capacity:
            current_weight += arr[i][1]
            t_profit += arr[i][0]

        else:
            remaining = capacity - current_weight
            cost = (arr[i][0] / arr[i][1]) * remaining
            t_profit += cost
            break

    return t_profit


# input
value = [60, 100, 200, 100]
weight = [10, 50, 50, 20]
capacity = 90

profit = fractional_knapsack(value, weight, capacity)

print("Total profit:", profit)
