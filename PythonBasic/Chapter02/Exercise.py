# 문제1
korean = 80
english = 75
math = 90
science = 95
sum = korean + english + math + science
average = sum / 4
print(average)

# 문제2
def check(number):
    if number % 2 == 1:
        print('홀수입니다.')
    else:
        print('짝수입니다.')

num = 13
check(num)
num2 = 16
check(num2)

# 문제3
rrn = '881120-1068234'
print(rrn[:6])
print(rrn[7:])

# 문제4
print(rrn[7])

# 문제5
word = 'a:b:c:d'
print(word.replace(':', '#'))

# 문제6
list  = ['우리', '끝까지', '힘내요!']
print(' '.join(list))