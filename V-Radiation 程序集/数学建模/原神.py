p = 0.006
dp = 0.06
x = list(range(1, 90))
ex1 = []
ex2 = []
p2 = [p+0.06 * (i-73) for i in range(74, 90)]
for i in x:
    if i >= 74:
        p += dp
    if i != 1 and i < 74:
        s = i * ((1 - p) ** (i - 1)) * p
    elif i >= 74:
        s = i * p * (0.994 ** 73)
        for j in range(i-74):
            s *= (1-p2[j])
    else:
        s = i * p
    ex1.append(s)

pe = (0.994 ** 73) * 1 * 90
for jf in p2:
    pe *= (1-jf)
ex1.append(pe)
print("E(X)" + str(sum(ex1)))
