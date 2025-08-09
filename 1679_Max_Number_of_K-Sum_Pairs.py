class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0 
        nums.sort()
        r = len(nums) - 1
        count = 0 
        while l < r:
            sum = nums[l] + nums[r]
            if sum == k:
                l += 1
                r -= 1
                count += 1
            elif sum < k:
                l += 1
            else:
                r -= 1

        return count
