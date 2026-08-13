array = [10, 25, 30, 45, 50] # initialize the list
index = -10  # index variable to store the index of target
found = False  # boolean variabel to determine if target is found or not

target = int(input("Enter the value you want to search: "))  # input the target value

for i in range(0, len(array)):
    if array[i] == target:
        index = i                # if target is found, store its index
        found = True

if found:
    print("Element found at index:", index)   # if found, print index
else:
    print("NOt found")                        # else print not found