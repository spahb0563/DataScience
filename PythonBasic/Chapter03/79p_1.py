sum = 0
print('수열 =', end=' ')
for i in range(1, 101) :
    if i%2 != 0 and i%3 == 0 :
        print(i, end=' ')
        sum += i
print()
print(f'누적합 = {sum}')