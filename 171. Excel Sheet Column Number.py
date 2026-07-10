columnTitle = "AZ"
d={}
t= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
    # d[t[i]]=i+1
    d[i] = t[i]
print(d)

# count = 1
# column_number = 0
# for i in columnTitle[::-1]:
#     column_number += (count*d[i])
#     count *=26
# print(column_number)
