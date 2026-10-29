n = 8
dp = [-1] * (n+1)

def fibonacci (n, dp):
    if n <=1:
        return n  

    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
        
    return dp[n]

print("fibonacci of 8 is: " , fibonacci(n, dp))

print(dp)

