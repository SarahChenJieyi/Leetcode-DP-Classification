import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # dynamic programming solution
        # each element in dp list stand for the maximum subarray sum end with current element
        dp = list(nums) # for deep copy
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + dp[i], dp[i])

        return max(dp)


if __name__ == '__main__':
    result = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)