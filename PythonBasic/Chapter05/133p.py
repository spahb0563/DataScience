x = 50;

def local_func(x):
    x += 50
    print(f'지역변수 x:{x}')

def print_x():
    print(f'함수에서 전역함수 읽기 시도: {x}')
    x += 50

local_func(x)
print(f'전역변수 x:{x}')
print_x()

num = 10

if True:
    num
