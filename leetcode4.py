class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getemptyanswer(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) % 2:
                return nums[(len(nums)-1)//2]
            else:
                return (nums[len(nums)//2-1] + nums[len(nums)//2])/2
        if not nums1:
            return getemptyanswer(nums2)
        if not nums2:
            return getemptyanswer(nums1)
        if (len(nums1) + len(nums2)) % 2:
            nums1.extend(nums2)
            nums1.sort()
            return nums1[(len(nums1)-1)//2]
        if (len(nums1) + len(nums2)) % 2 == 0:
            nums1.extend(nums2)
            nums1.sort()
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2
