class Solution:
    def totalMoney(n) :
        money_total = 0
        monday_value =0
        for i in range(n):
            if(i%7==0):
                monday_value +=1
            money_total += i%7 + monday_value
        return money_total

print(Solution.totalMoney(10))
print(Solution.totalMoney(4))
print(Solution.totalMoney(20))