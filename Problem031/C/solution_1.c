/*
 * =====================================================================================
 *
 *                      Copyright 2015 Manoel Vilela
 *
 *
 *       Filename: solution_1.c
 *
 *    Description: Solution for Problem031 of ProjectEuler
 *
 *         Author: Manoel Vilela
 *        Contact: manoel_vilela@engineer.com
 *   Organization: UFPA
 *     Perfomance: 0.02s | Intel E7400 @ 3.5Ghz
 *
 * =====================================================================================
**/

#include <stdio.h>
#define N_COINS 8

int different_ways(int money, int *coins, int n_coins) {
    int max_coin = money / (*coins);
    int n, ways = 0;
    for (n = 0; n <= max_coin; n++) {
        int new_money = (*coins) * n;

        if (n_coins > 1 && new_money < money)
            ways += different_ways(money - new_money, coins + 1, n_coins - 1);

        if (new_money == money) {
            ways++;
            break;
        }
    }

    return ways;
}


int main(int argc, char **argv){
    int coins[N_COINS] = {200, 100, 50, 20, 10, 5, 2, 1};
    int money = 200;
    int answer = different_ways(money, coins, N_COINS);

    printf("%d\n", answer);
    return 0;
}