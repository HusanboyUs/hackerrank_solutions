nums = [3,2,3]

def majorityNum(nums):
    store ={}
    for indx,ele in enumerate(nums):
        a=nums.count(ele)

        store[indx] = a
    m = max(store.values())
    print(max(store.values()))
    print(store)
    return f"{nums.index(m) , 'answer' }" 



print(majorityNum(nums))    