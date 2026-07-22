class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if(i in 'aeiouAEIOU'):
                vowels.append(i)
        vowels.sort()
        k=0
        s1=""
        for i in s:
            if(i not in 'aeiouAEIOU' ):
                s1 += i
            else:
                s1 += vowels[k]
                k+=1
        return s1
