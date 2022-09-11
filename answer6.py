#program to print middle digit of a three digit number 
x=int(input("Enter a three digit number : ")) 
number=x/10
middlenum=number%10
print("Middle number =%d"%middlenum)