class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        length = len(nums)
        
        pre = nums[0]
        end = 0
        # find the right-most unorder pos
        for i in range(length):
            if (nums[i] < pre):
                end = i
            else:
                pre = nums[i]
        
        pre = nums[-1]
        start = length -1
        # find the left-most unorder pos
        for i in range(length-1, -1, -1):
            if (nums[i] > pre):
                start = i
            else:
                pre = nums[i]
        

        return end - start + 1 if end != 0 else 0
