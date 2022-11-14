#<조건1> 수량 변수 : su = 5
#<조건2> 단가 변수 : dan = 800
#<조건3> su, dan 변수 주소 확인
#<조건4> 금액 계산 = 수량 x 단가
#<조건5> 기타 세부내용<출력 화면 예시> 참고

su = 5
dan = 800
print("su 주소 : " + str(id(su)))
print("dan 주소 : " + str(id(dan)))
print("금액 : " + str(su*dan))

