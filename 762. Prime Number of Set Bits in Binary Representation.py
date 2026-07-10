class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes =[True]*(34)
        primes[0]=False
        primes[1]=False
        for i in range(2,33):
            if(primes[i]):
                for j in range(i*i,len(primes),i):
                    primes[j]=False
        l=[0]*256
        count_primes = 0
        for i in range(256):
            l[i] = (i&1) + l[i//2]
        for i in range(left,right+1):
            set_bits = l[i&0xff] + l[(i>>8)&0xff] +l[(i>>16)&0xff] +l[(i>>24)] 
            if(primes[set_bits]):
                count_primes +=1
        return count_primes
