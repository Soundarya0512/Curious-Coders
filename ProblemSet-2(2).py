# Prob 2:

# Write a program to take x and print multiples of x till 1000.

x=int(input("Enter the value for x: "))

i=1
c=0
while x*i<=1000:
    print(x*i)
    i=i+1
    c=c+1
print("c",c)

c1=0
c2=0
x=int(input("Enter the value for x: "))
for i in range(x,1001,x):
    c1=c1+1
    if i%x==0:
        c2=c2+1
        print(i)
print("c1",c1)
print("c2",c2)