class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0

        # initial DP table
        # dp[i][j] represent the length of LCS in text1[:j+1] and text2[:i+1] 
        dp = [([0] * len(text1)) for _ in range(len(text2))]
        # base case
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, len(text2)):
            if text2[i] == text1[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, len(text1)):
            if text1[j] == text2[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]
        # dynamic programming
        # state transition equation: dp[i][j] =
        #                                       max(text1[:j+1] and text2[:i] LCS, text1[:j] and text2[:i+1] LCS)
        #                                       text1[:j] and text2[:i] LCS + 1 (if text1[j] == text2[i])
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
