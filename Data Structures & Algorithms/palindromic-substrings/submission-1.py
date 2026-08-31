class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return len(s)
        
        dp = [[False] * n for _ in range(n)]
        
        count = 0
        
        for i in range(n):
            dp[i][i] = True
        
        # Length 2 checks
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
        
        #Length 3+ checks: DP
        for L in range(3,n+1):
            for i in range(n-L+1):
                j = i + (L-1)  #LAst possible idx
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True

        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        return count
        