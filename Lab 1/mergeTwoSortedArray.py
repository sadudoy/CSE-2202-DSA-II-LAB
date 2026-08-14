array1 = [] 
array2 = []                                                  # declare the arrays
merged = [] 

size1 = int(input("Enter the size of the first array: "))    # input the size of the arrays
size2 = int(input("Enter the size of the second array: "))

print("Enter the first array: ")
for i in range (0, size1):                                   # input the elements of both arrays
    array1.append(int(input()))

print("Enter the second array: ")
for i in range (0, size2):
    array2.append(int(input()))


merged = array1.copy()                                      # copy array1 into merged so that the original array1 remains intact

i = 0
j = 0

while j < size2:
    if i < len(merged) and merged[i] < array2[j]:           # check if the i th element of merged is less than 
        i += 1                                              # the j th element of array2, if so , increment i
    else:                                                   # again check, if the element of array2 is smaller, 
        merged.insert(i, array2[j])                         # then insert into the i th postition of merged array
        j += 1                                              # and increment both i and j
        i += 1

print("The merged sorted array: ", merged)
