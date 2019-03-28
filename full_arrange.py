import json

def full_arrange(res,nums,index):
    if index == len(nums):
        if not nums in res:
            res.append(nums[:])
            print(nums)
            # counter += 1
            return
    for i in range(index,len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        full_arrange(res, nums, index + 1)
        nums[i], nums[index] = nums[index], nums[i]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    res = []
    full_arrange(res, nums, 0)
    print(res)
    dict_res = {}
    for k, v in enumerate(res):
        dict_res[k] = v
    with open("./full_arrange.json", "w") as json_f:
        json.dump(dict_res, json_f)
        print("write finish!")
if __name__ == '__main__':
    main()