class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        fact = [1]
        for i in range(1,rowIndex+1):
            fact.append(i*fact[i-1])
        ans =[]
        row_fact_val = fact[rowIndex]
        for i in range(rowIndex+1):
            fact_val = fact[rowIndex-i]
            c_val = fact[i]
            base_value = (fact_val*c_val)
            ans.append((row_fact_val) // base_value)
        return ans
