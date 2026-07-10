def findKthBit( n, k):
     l=["0"]*(n+1)
     l[0]="0"
     l[1]="0"
     for i in range(2,n+1):
          inverts_str = invert(l[i-1])
          l[i] = l[i-1] + '1' + inverts_str[::-1]
     print(l)
          
def invert(s):
        s1= ""
        for i in s:
            if(i=='0'):
                s1+='1'
            else:
                s1+='0'
        return s1
findKthBit(n=3,k=1)