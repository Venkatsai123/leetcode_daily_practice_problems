triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
low_index =0
sum_of_triangle = 0
for i in triangle:
    if(len(i)==1):
        sum_of_triangle += i[low_index]
    else:
        sum_of_triangle += min(i[low_index],i[low_index+1])
        if(i[low_index]>i[low_index+1]):
            low_index += 1
        else:
            low_index = low_index
        
    print(low_index, sum_of_triangle)
print(sum_of_triangle)