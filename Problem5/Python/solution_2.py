#Some milliseconds slower than solution 1
def div20(num):
    return all([num%x==0 for x in range(20, 10, -1)])
num = 2520
while True:
    if div20(num):
        print(num)
        break
    num+=2520
