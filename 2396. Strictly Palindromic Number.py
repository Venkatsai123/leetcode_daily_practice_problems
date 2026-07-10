def isStrictlyPalindromic( n):
    for i in range(2, n-1):
        base_rep = ""
        num = n
        while num > 0:
            base_rep += str(num%i)
            num=num//i
        print(base_rep)
        if(base_rep[::-1]!=base_rep):
            return False
    return True
# print(isStrictlyPalindromic(9))

print(isStrictlyPalindromic(4))