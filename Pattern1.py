n =int(input("Enter number of rows:"))

# for i in range(num):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()



