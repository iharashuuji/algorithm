# 条件付きカウント 特殊な記法について
arr = [1, 2, 3, 4, 5, 6]
count_evens = sum(1 for num in arr if num % 2 == 0)
print(count_evens)  # 3


# 貪欲法
coins = [10, 5, 1]
amount = 17
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)  # 4 (10円1枚, 5円1枚, 1円2枚)