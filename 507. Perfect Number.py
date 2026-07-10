num = int(input("Enter the number: "))

i=2
while i*i <num:
    if(num%i==0):
        print(i)
        if(num//i != i):
            print(num//i)
    i += 1