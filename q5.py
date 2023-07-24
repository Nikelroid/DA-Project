import sys
def find_longest_incraseing_common_subsequence(a, n, b, m):
    dp = [0 for i in range(m)]
    for i in range(n):
        pos = 0
        for j in range(m):
            dp[j] = pos + 1 if a[i] == b[j] and pos + 1 > dp[j] else dp[j]
            pos = dp[j] if a[i] > b[j] and dp[j] > pos else pos
    result = 0
    for i in range(m):
        result = dp[i] if dp[i] > result else result

    return result

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

print(find_longest_incraseing_common_subsequence(a, n, b, m))