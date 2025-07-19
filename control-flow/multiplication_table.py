number = int(input("Enter a number to see its multiplication table: "))
for item in range(1, 11):
    result = item * number
    print(number,"*",item,"=",result)
