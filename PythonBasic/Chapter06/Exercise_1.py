#p183

#[문제1]

class Rectangle :

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return area

    def circum_calc(self):
        circum = (self.width+self.height) * 2
        return circum

#[출력결과]

print('사각형의 넓이와 둘레를 계산합니다.')

width = int(input('사각형의 가로 입력 : '))
height = int(input('사각형의 세로 입력 : '))

print('-'*30)

rectangle = Rectangle(width, height)
print(f'사각형의 넓이 : {rectangle.area_calc()}')
print(f'사각형의 둘레 : {rectangle.circum_calc()}')

print('-'*30)
