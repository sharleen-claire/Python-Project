
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
thrd = int(input("Enter the third number: "))

if first > second and first > thrd:
    print(first ,"is the largest number")

elif second > first and second > thrd:
    print(second ,"is the largest number")

else:
    print(thrd ,"is the largest number")

