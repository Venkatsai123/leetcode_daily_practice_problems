class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n =len(nums)
        for i in range(1<<n):
            if(format(i,f'0{n}b') not in nums):
                return format(i,f'0{n}b')
