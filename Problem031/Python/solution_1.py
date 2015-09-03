#!/usr/bin/env python
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#
#   Answer: 73682 @ 0.6s
#   Hardware:Intel E7400 @ 3.5Ghz


# black magic recursive
def different_ways(money, coins, summation=0):
    ways = 0
    max_coins_head = money // coins[0]
    for n in range(max_coins_head + 1):
        new_money = n * coins[0]
        if len(coins) > 1 and new_money < money:
            ways += different_ways(money - new_money, coins[1:], new_money)
        if new_money == money:
            ways += 1
            break
    return ways


def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    money = 200
    solution = different_ways(money, coins)
    print(solution)


if __name__ == '__main__':
    main()
