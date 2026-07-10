n=8
i=0
j=8
while i<j:
    mid = (i+j)//2
    expo = int(mid*mid)
    if(mid*mid == n):
        print(mid)
        break
    elif(mid*mid < n):
        i=j+1
    elif(mid*mid >n):
        j=i-1