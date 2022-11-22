#[문제1]

lst = [10, 1, 5, 2]

result = lst * 2

print(result)

result.append(lst[0]*2)

print(result)

result = result[::2]

print(result)

#[문제2]

size = int(input('vector 수 : '))
list = []

for i in range (size) :
    list.append(int(input()))

print(f'vector 크기 : {len(list)}')

size = int(input('vector 수 : '))
list = []

for i in range (size) :
    number = int(input())
    if number in list :
        print('YES')
    list.append(number)

#[문제3]
message = ['spam', 'ham', 'spam', 'ham', 'spam']

dummy = [1 if msg == 'spam' else 0 for msg in message]

print(dummy)

spam_list = [msg for msg in message if msg == 'spam']

print(spam_list)

#[문제4]

position = ['과장', '부장', '대리', '사장', '대리', '과장']

uni_position = list(set(position))
print(f'충복되지 않은 직위 : {uni_position}')

position_cnt = {}
for p in position :
    position_cnt[p] = position_cnt(p, 0) + 1
print(position_cnt)