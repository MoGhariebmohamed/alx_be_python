length = int(input("Enter the size of the pattern: "))
start = 1
while start <= length:
    for item in range(0, length):
        print("*", end="")
    start += 1
    print("")
    