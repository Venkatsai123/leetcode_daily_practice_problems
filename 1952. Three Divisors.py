class Solution:
    def isThree(self, n: int) -> bool:
        if(n<3):
            return False
        i=1
        count = 0
        while i <= n :
            if(n%i==0):
                count+=1
            i+=1
        return True if count==3 else False
