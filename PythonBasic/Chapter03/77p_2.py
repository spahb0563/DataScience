weight = int(input('짐의 무게는 얼마입니까 ?'))
fee = 0
if weight >= 10 :
    fee = (weight // 10) * 10000
    print(f"수수료는 {format(fee, ',')}원 입니다.")
else :
    print("수수료는 없습니다.")
