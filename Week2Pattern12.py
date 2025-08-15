N=3
i = 1
while i <= N-1:
    j = 1
    while j <= N - i:
        print(" ", end='')
        j += 1
    j = 1
    while j <= (i * 2) - 1:
        print("*", end='')
        j += 1
    print()
    i += 1

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

