def plusOne(digits):
    no_of_digits = len(digits)-1
    n1 = 0
    for i in digits:
        n1 += i*(10**no_of_digits)
        no_of_digits -=1
    n1 = n1+1
    plusone_number =[]
    while n1>0:
        plusone_number.append(n1%10)
        n1//=10
    print(plusone_number[::-1])

    

digits = [1,2,3]
plusOne(digits=digits)