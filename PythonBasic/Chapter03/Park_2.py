while True:
    age = int(input('나이를 입력해주세요 : '))

    if age < 0 :
        print('나이 입력 오류')
        continue

    fee = 0
    grade = ''
    if 0 <= age <= 3 :
        grade = '유아'
    elif 4 <= age <= 13:
        grade  = '어린이'
        fee = 2000
    elif 14 <= age <= 18:
        grade = '청소년'
        fee = 3000
    elif 19 <= age <= 65:
        grade = '성인'
        fee = 5000
    else :
        grade = '노인'

    if fee == 0:
        print(f'귀하는 {grade}등급이며 요금은 무료입니다.')
    else:
        print(f'귀하는 {grade}등급이며 요금은 {fee}원 입니다.')
