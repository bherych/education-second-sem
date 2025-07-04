import math

def max_wire_length(w, heights):
    n = len(heights)
    
    dp = [{} for _ in range(n)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0.0

    for i in range(1, n):
        for h in range(1, heights[i] + 1):
            max_len = 0.0
            for h_prev in dp[i - 1]:
                dist = math.sqrt(w ** 2 + (h - h_prev) ** 2)
                max_len = max(max_len, dp[i - 1][h_prev] + dist)
            dp[i][h] = max_len

    return round(max(dp[n - 1].values()), 2)

print(max_wire_length(2, [3, 3, 3]))                          
print(max_wire_length(100, [1, 1, 1, 1]))                      
print(max_wire_length(4, [100, 2, 100, 2, 100]))               
print(max_wire_length(4, [56, 18, 17, 94, 23, 7, 21, 94, 29,
                          54, 44, 26, 86, 79, 4, 15, 5, 91,
                          25, 17, 88, 66, 28, 2, 95, 97, 60,
                          93, 40, 70, 75, 48, 38, 51, 34, 52,
                          87, 8, 62, 77, 35, 52, 3, 93, 34,
                          57, 51, 11, 39, 72]))               
