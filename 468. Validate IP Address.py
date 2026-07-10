def validIPAddress(queryIP):
    if(queryIP.count('.')==3):
        ipv4 = queryIP.split('.')
        c=0
        for i in ipv4:
            if not (i.isdigit() and 0<=int(i)<=255):
                    c=c+1
        for i in ipv4:
             if len(i)>1 and i[0]=='0':
                  c=c+1

        return "IPv4" if c==0 else "Neither"
    elif(queryIP.count(':')==7):
        ipv6 = queryIP.split(':')
        c= 0 
        for i in ipv6:
            if not (1<=len(i)<=4 and i.isalnum()):
                c = c+1
            for j in "ghijklmnopqrstuvwxyz":
                 if (j in i.lower()):
                      c +=1
        print(c)
        return "IPv6" if c==0 else "Neither"

    else:
        return "Neither"
print(validIPAddress("172.16.254.1"))
print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print(validIPAddress("256.256.256.256"))
# print(validIPAddress("192.168@1.1"))
# print(validIPAddress("1e1.4.5.6"))
# print(validIPAddress("192.168.01.1"))
print(validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))