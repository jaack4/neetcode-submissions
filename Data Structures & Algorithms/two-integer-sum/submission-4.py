class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, num in enumerate(nums):
            nums_dict[num] = index

        for index, num in enumerate(nums):
            needed = target - num
            if needed in nums_dict and index != nums_dict[needed]:
                return sorted([index, nums_dict[needed]])
        

        