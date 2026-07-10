class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_of_divisors = 0
        for i in nums:
            j=1
            count = 0
            sum_div = 0
            while j*j <= i:
                if(i%j==0):
                    sum_div += j
                    count +=1
                j +=1
            j -=1
            if(j*j ==i):
                j-=1
            while j>=1:
                if(i%j==0):
                    sum_div +=(i//j)
                    count +=1
                j-=1
            if(count==4):
                sum_of_divisors += sum_div
        return sum_of_divisors
