MOD = 10**9+7
s = input()
t = 'chokudai'
dp = []
for i in range(len(s)+1):
    dp.append([0]*9)
for i in range(len(s)+1):
    dp[i][0] = 1 # 番兵
for i in range(len(s)):
    for j in range(8):
        if s[i] != t[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1]+dp[i][j]
        dp[i+1][j+1] %= MOD
print(dp[len(s)][8])