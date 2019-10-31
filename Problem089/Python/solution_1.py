from collections import Counter
from operator import itemgetter

units = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def check_valid_roman(string: str) -> int:
    c = Counter(string)
    only_once = ['D', 'L', 'V']
    invalid = {
        'IIIIIIIIII',
        'XXXXXXXXXX',
        'CCCCCCCCCC',
        'VV',
        'DD',
        'LL',
    }

    for k in only_once:
        if c.get(k, 0) > 1:
            return False

    for rule in invalid:
        unit = rule[0]
        if c.get(unit, 0) >= len(rule):
            return False

    return True


def parse_roman(string: str) -> int:
    codification = list(map(units.get, string))
    signal = []
    for i in range(len(codification) - 1):
        if codification[i] >= codification[i+1]:
            signal.append(+1)
        else:
            signal.append(-1)
    signal.append(1)
    number = 0
    for c, s in zip(codification, signal):
        number += c * s

    return number


def to_roman(integer: int) -> str:
    characters_by_unit = sorted(units.items(),
                                reverse=True,
                                key=itemgetter(1))
    roman = ''
    for c, unit in characters_by_unit:
        while integer - unit >= 0:
            roman += c
            integer -= unit
        if c in ('X', 'V') and integer - unit + 1 >= 0:
            roman += 'I' + c
            integer -= units[c] - 1
        elif c in ('L', 'C') and integer - unit + 10 >= 0:
            roman += 'X' + c
            integer -= units[c] - 10
        elif c in ('D', 'M') and integer - unit + 100 >= 0:
            roman += 'C' + c
            integer -= units[c] - 100

        if integer == 0:
            break

    return roman


def main():
    with open('../p089_romans.txt') as f:
        romans = list(map(str.strip, f.readlines()))
        reduced = [to_roman(parse_roman(r)) for r in romans]

        # # inconsistency check
        # for r1, r2 in zip(romans, reduced):
        #     v1, v2 = parse_roman(r1), parse_roman(r2)
        #     if v1 != v2:
        #         print(r1, r2, parse_roman(r1), parse_roman(r2))

        print(len(''.join(romans)) - len(''.join(reduced)))


if __name__ == '__main__':
    main()
