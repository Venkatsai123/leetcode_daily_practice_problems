def numSquares( n):
    i=1
    l={}
    while i*i<=n:
        l[i*i] = i
        i+=1
    