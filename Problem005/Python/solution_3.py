# someone in the internet do that

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i * j) % k == 0:
                i *= j
                break
print(i)
