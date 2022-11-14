# 공원 ver4
while True :
    age = int(input('나이를 입력하세요.'))
    if age < 0:
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

        payment_method = int(input('요금 유형을 선택하세요.(1: 현금, 2: 공원 전용 신용 카드)'))

        if payment_method == 1:
            while True:
                pay = int(input('요금을 입력하세요.'))

                if pay < 0:
                    print('요금 입력 오류')
                    continue

                if fee > pay:
                    print(f'{fee - pay}원이 모자랍니다. 입력 하신 {pay}원을 반환 합니다.')
                elif fee < pay:
                    print(f'감사합니다. 티켓을 발행하고 거스름돈 {pay - fee}원을 반환 합니다.')
                else:
                    print('감사합니다. 티켓을 발행합니다.')
                break
        elif payment_method == 2:
            if 60 <= age <= 65:
                fee *= 0.85
            else:
                fee *= 0.9
        print(f'{int(fee)}원 결제 되었습니다. 티켓을 발행합니다.')


