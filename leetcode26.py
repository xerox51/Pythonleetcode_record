class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictnums = {}
        for i in range(len(nums)):
            dictnums[nums[i]] = i
        listnums = list(dictnums.keys())
        for j in range(len(listnums)):
            nums[j] = listnums[j]
        nums = nums[0:len(listnums)]
        return len(nums)
