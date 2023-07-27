mt = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
x_sum = 0
y_sum = 0
for i in range(len(mt)):
    x_sum += mt[i][i]

for i in range(len(mt)):
    y_sum += mt[i][len(mt)-1-i]


print(x_sum-y_sum)
