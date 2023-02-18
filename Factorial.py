import math

n=int(input("Enter any number:"))

#inbuilt function
# result=math.factorial(n)
# print(result)


#recurrsion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
result=fact(n)
print(result)
