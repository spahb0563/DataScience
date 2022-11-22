#[1]

lst = [1, 3, 5, 4, 2]

lst.sort(reverse=True)

print(lst)


#[2]
t = (1, 2, 3)

lst = list(t)

lst.append(4)

t = tuple(lst)

print(t)

#[3]

a = {'A': 90, 'B': 80, 'C': 70}

a.pop('B')

print(a)

#[4]

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

a_set = set(a)

print(a_set)

#[5]

point = {'kim99': 12000, 'lee66': 11000, 'han55': 3000, 'hong77': 5000, 'hwang33': 18000}

for index, key in enumerate(point.keys()):
    print(f'{index+1}. 아이디 : {key}, 마일리지 : {point[key]} 점')

#[6]

KEY = 'han55'
p = 5000

for key in point.keys():
    if key == KEY:
        point[key]= p

print(point)

point[KEY]=point.get('hong77')

print(point)

point[KEY] = p

print(f'{KEY}님의 마일리지가 {p}점으로 수정되었습니다.')

#[7]
name = 'jang88'
p = 7000

point[name] = p
print(f'전체 딕셔너리 : {point}')
print(f'{name}님의 마일리지 ({p}점)가 추가되었습니다.')

#[8]
max_point = 0
max_user = ''

for key in point.keys() :
    if max_point < point[key] :
        max_point = point[key]
        max_user = key

print(f'{max_user}님의 {max_point}점이 가장 높은 점수입니다.')

#[9]

temperatures = {'월': 25.5, '화': 28.3, '수': 33.2, '목': 32.1, '금': 17.3, '토': 35.3, '일': 33.3}

print("-----------------------------------------------------")
for key in temperatures.keys():
    print(f"  {key}",end='\t')
print("\n-----------------------------------------------------")
for key in temperatures.keys():
    print(f" {temperatures[key]}",end='\t')
print("\n-----------------------------------------------------")

#[10]

print(f'가장 낮은 최고 기온 : {min(temperatures.values())}˚')

#[11]

result = []

for key in temperatures.keys():
    if temperatures[key] >= 30 :
        result.append(key)
print(f"기온이 30˚ 이상인 요일 : {','.join(result)}")

#[12]

temperatures_sum = sum(temperatures.values())

length = len(temperatures)

print(f'일주일간 최고 기온의 평균 : {round(temperatures_sum / length, 1)}˚')

#[13]
# 다음의 영수의 기말고사 성적이다.
# 가장 높은 점수를 받은 과목, 가장 낮은 점수를 받은 과목의 과목명과 점수를 출력하고 평균점수를 구하여라
score = {'국어': 80, '수학': 95, '영어': 65, '과학': 74, '역사': 70}

max_score = max(score.values())
max_score_subject = ''
min_score = min(score.values())
min_score_subject = ''

score_sum = sum(score.values())
length = len(score)

for key in score.keys() :
    s = score[key]
    if s == max_score :
        max_score_subject = key
    elif s == min_score :
        min_score_subject = key

print(f'가장 높은 점수를 받은 과목은 {max_score_subject}이며 {max_score}점을 받았습니다.')
print(f'가장 낮은 점수를 받은 과목은 {min_score_subject}이며 {min_score}점을 받았습니다.')
print(f'평균 점수는 {score_sum / length}점 입니다.')
