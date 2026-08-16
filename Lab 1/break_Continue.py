fruits = ["apple", "banana", "jackfruit", "mango"]

for fruit in fruits:
    if(fruit == "banana"):
        break
    print(fruit, end=" ")

print()

for fruit in fruits:
    if(fruit == "banana"):
        continue
    print(fruit, end=" ")

