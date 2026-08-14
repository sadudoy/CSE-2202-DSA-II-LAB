array = []                                                      # declare the list
index = -1                                                      # index variable to store the index of target
found = False                                                   # boolean variable to determine if target is found or not

size = int(input("Enter the size of the list: "))

print("Enter the elements- ")

for i in range(0, size):
    array.append(int(input()))                                  # input list elements

target = int(input("Enter the value you want to search: "))     # input the target value

for i in range(0, size):
    if array[i] == target:
        index = i                                               # if target is found, store its index
        found = True

if found:
    print("Element found at index:", index)                     # if found, print index
else:
    print("NOt found")                                          # else print not found