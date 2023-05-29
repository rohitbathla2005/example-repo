for i in range (0,5):
    for j in range (0, i+1):
        print ("*",end="")

    print()


for i in range (0,5):
    for j in range (0, i+1):
        print (j,end="")

    print()
n=1
for i in range (0,5):
    for j in range (0, i+1):
        print (n,end="")
        n=n+1
    print()

n=65
for i in range (0,5):
    for j in range (0, i+1):
        c=chr(n)
        print (c,end="")
        n=n+1
    print()