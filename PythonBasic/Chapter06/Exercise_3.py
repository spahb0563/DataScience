#[문제3]

class Person:

    name = gender = None
    age = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f'이름 : {self.name}, 성별 : {self.gender}')
        print(f'나이 : {self.age}')


name = input('이름 입력 : ')
age = int(input('나이 입력 : '))
gender = input('성별(male/female) 입력 : ')

print('='*30)
p = Person(name, age, gender)
p.display()
print('='*30)