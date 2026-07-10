def checkPrimeFrequency(nums):
        from collections import Counter
        dict_count = Counter(nums)
        prime_count = 0
        for val , frq in dict_count.items():
                if(frq==1):
                      continue
                else:
                    i=1
                    count =0
                    while i*i <= frq:
                        if(frq%i==0):
                                count +=1
                        i=i+1
                    if(count == 1):
                          prime_count +=1
        return prime_count > 0
nums = [1,2,3,4,5,4]
print(checkPrimeFrequency([1,2,3,4,5,4]))
print(checkPrimeFrequency([1,2,3,4,5]))
print(checkPrimeFrequency([2,2,2,4,4]))
print(checkPrimeFrequency([3,0,3,6,3,3]))