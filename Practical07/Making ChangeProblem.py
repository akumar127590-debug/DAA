n = int(input("Enter number of coins: "))

print("Enter coin values:")
coins = list(map(int, input().split()))

amount = int(input("Enter amount: "))

if len(coins) != n:
    print("Invalid input")
else:
    dp = [99999] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)

    if dp[amount] == 99999:
        print("Change not possible")
    else:
        print("Minimum coins:", dp[amount])
