# 1~100
for i in range(1, 101):
    print(i, end=' ')

print()
# whilt 1 ~1000 3 배수 합

sum = 0
i = 1
while i <= 1000:
    sum += i
    i += 1
print(f'1000까지 3의 배수의 합 {sum}')

# 평균 점수
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in scores:
    sum += score
average = sum / len(scores)
print(f'평균 점수 {average}')

print()
# 삼각형 ver1
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()

# 삼각형 ver2
for i in range(5):
    for j in range(4 - i):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()