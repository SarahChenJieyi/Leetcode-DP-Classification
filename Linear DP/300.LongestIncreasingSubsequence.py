class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # initial dp list
        # elements in dp represent the current longest increasing subsequence end with curren num
        dp = [1] * len(nums)
        glo_max = 1
        for i in range(1, len(nums)):
            cur_max = 1
            for j in range(i):
                if nums[j] < nums[i]: # nums[i] can be the element follow nums[j]
                    cur_max = max(cur_max, dp[j] + 1)
            dp[i] = cur_max
            glo_max = max(glo_max, cur_max)
        return glo_max
