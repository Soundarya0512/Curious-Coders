# Prob 3:
# Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.

firstname=input("Enter the first name: ")
lastname=input("Enter the last name: ")
n=int(input("Enter value of n: "))

for i in range(n):
    print("FullName is: ",firstname+lastname)