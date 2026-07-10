def containsNearbyDuplicate( nums, k) :
    dict_num = {}
    for i in range(len(nums)):
        if(dict_num.get(nums[i]) != None):
            print(dict_num,i, nums[i])
            if(abs(i - dict_num[nums[i]]) <= k):
                return True
        else:
            dict_num[nums[i]] = i
        print(dict_num,i, nums[i])
        # print(dict_num,i,nums[i],dict_num[nums[i]])
    return False
# nums = [1,2,3,1]
# k = 3
# print(containsNearbyDuplicate(nums=nums,k=k))

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums=nums,k=k))