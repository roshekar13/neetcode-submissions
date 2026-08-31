class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        for i in range(n):
            dp[i][i] = True
        
        # Length 2 checks
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        
        #Length 3+ checks: DP
        for L in range(3,n+1):
            for i in range(n-L+1):
                j = i + (L-1)  #LAst possible idx
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_len = L
 
        return s[start:start+max_len]
        



