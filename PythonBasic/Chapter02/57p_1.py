#<조건1> 지방,탄수화물,단백질의 그램을 키보드로 입력받는다.
#<조건2> 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4

fat = int(input('지방의 그램을 입력하세요 : '))
carbohydrate = int(input('탄수화물의 그램을 입력하세요 : '))
protein = int(input('단백질의 그램을 입력하세요 : '))
totalCal = fat * 9 + carbohydrate * 4 + protein * 4
print('총 칼로리 : ' + format(totalCal, ',') + 'cal')