from collections import Counter

hands = [line.split(' ') for line in open('p054_poker.txt')]

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
straights = [(v, v - 1, v - 2, v - 3, v - 4) for v in range(14, 5, -1)]
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1)]

def calculate_rank(hand):
    score = list(zip(*sorted(((v, values[k]) for k, v in Counter(x[0] for x in hand).items()), reverse=True)))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5  # flush
    if score[1] in straights:
        score[0] = 4  # straight
    return score

p1_wins = sum(calculate_rank(hand[:5]) > calculate_rank(hand[5:]) for hand in hands)

print(f'P1 wins {p1_wins} times')
