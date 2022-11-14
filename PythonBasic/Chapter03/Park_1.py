# 더조은 it 공원 입장료

while True :
    age = int(input('나이를 입력해주세요 : '))


    if age < 0 :
        print('나이 입력 오류')
        continue
    fee = 0

    if 4 <= age <= 13:
        fee = 2000
    elif 14 <= age <= 18:
        fee = 3000
    elif 19 <= age <= 65:
        fee = 5000

    if fee == 0:
        print('요금은 무료입니다.')
    else:
        print(f'요금은 {fee}입니다.')