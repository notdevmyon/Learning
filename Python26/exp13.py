Age=int(input("Enter Age: "))
if Age>=18:
    print("The person can vote")
else:
    print("Person Can't Vote")
    print("Wait for ",18-Age,"Years")