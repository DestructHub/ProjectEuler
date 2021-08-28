from lib.digital import digit_sum
from lib.sequence import Factorials

# Compute the answer to Project Euler's problem #20 


def solve():
    target = 100
    factorials = Factorials()
    x = factorials[target]
    answer = digit_sum(x)
    return answer


#expected_answer = 648
