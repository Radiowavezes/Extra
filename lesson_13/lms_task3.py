def choose_func(nums):
    nums = sorted(nums)
    def square_nums():
        return [num ** 2 for num in nums]
    def remove_negatives():
        return [num for num in nums if num > 0]
    if nums[0] > -1:
        return square_nums
    else:
        return remove_negatives

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
res_pos = choose_func(nums1)
res_neg = choose_func(nums2)
print(res_pos())
print(res_neg())
