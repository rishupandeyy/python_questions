class Solution:
    def twoSum(self, nums, target):
        hashMap = {}  # number : index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i

nums_list = [2, 7, 11, 15]
target_value = 9

solution_obj = Solution()

result = solution_obj.twoSum(nums_list, target_value)
print(result)

nums_list_2 = [3, 2, 4]
target_value_2 = 6
result_2 = solution_obj.twoSum(nums_list_2, target_value_2)
print(result_2)