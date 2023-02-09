n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        ch = chr(64+i)

        if(i==1 or i==n or j==1 or j==n):
           print(ch,end=" ")
        else:
            print(" ",end=" ")
    print(' ')