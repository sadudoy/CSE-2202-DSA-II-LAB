age = int(input("enter your age: "))

if age>18:
    print("Is adult")
else:
    print("Not adult")

print()

marks = int(input("Enter marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
elif marks >= 50:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: F")