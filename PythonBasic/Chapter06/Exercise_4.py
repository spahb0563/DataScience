#[문제4]

class Employee:
    name = None

    pay = 0

    def __init__(self, name):
        self.name = name

class Permanent (Employee):

    def __init__(self, name, base_pay, bonus):
        super().__init__(name)
        self.pay = base_pay + bonus
class Temporary (Employee):

    def __init__(self, name, work_time, wage):
        super().__init__(name)
        self.pay = work_time * wage

empType = input('고용형태 선택(정규직<P>, 임시직<T>) : ')

if empType.upper() == 'P' :
    name = input('이름 :>? ')
    base_pay = int(input('기본급 :>? '))
    bonus = int(input('기본급 :>? '))
    print('='*30)

    employee = Permanent(name, base_pay, bonus)

    print('고용형태 : 정규직')
    print(f'이름 : {employee.name}')
    print(f"급여 : {format(employee.pay, ',')}")

elif empType.upper() == 'T' :
    name = input('이름 :>? ')
    work_time = int(input('작업시간 :>? '))
    wage = int(input('시급 :>? '))
    print('='*30)

    employee = Temporary(name, work_time, wage)

    print('고용형태 : 임시직')
    print(f'이름 : {employee.name}')
    print(f"급여 : {format(employee.pay, ',')}")
else :
    print('='*30)
    print('입력 오류')