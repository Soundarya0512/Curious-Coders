N=3
i=N
while i>0:
    j=N-i
    while j>0:
        print(" ",end='')
        j=j-1
    j=i*2-1
    while j>0:
        print("*",end='')
        j=j-1
    print()
    i=i-1