#program to print only first digit of a three digit number 
n=int(input("Enter any three digit number : "))
while(n>=10):
    n=n//10
print("the first digit of the number is %d"%n)
