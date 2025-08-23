n=int(input("Enter the number:"))
sum=0
while n>0:
    l=n%10
    sum=(sum*10)+l
    n=n//10
print("Reverse:",sum)