class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using sort
        nums = sorted(nums, reverse=True)
        return nums[k-1]
        
        # using bubble sort
        # for i in range(k):
        #     for j in range(len(nums)-1-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return nums[-k]
