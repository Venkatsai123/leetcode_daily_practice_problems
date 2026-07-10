def maximumProduct( nums) -> int:
    max_value_dict = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i!=j):
                max_value_dict[nums[i]*nums[j]]=[i,j]
    max_value =[]
    for i in range(len(nums)):
        for j in max_value_dict:
            if(i not in max_value_dict[j]):
                max_value.append(j*nums[i])
    print(max_value,max_value_dict)
    return max(max_value)

print(maximumProduct(nums=[-100,-98,-1,2,3,4]))