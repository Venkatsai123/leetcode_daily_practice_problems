def maximumOddBinaryNumber(num):
    for i in range(len(num)):
        for j in range(i,len(num)):
            print(num[i:j+1])
maximumOddBinaryNumber("52")