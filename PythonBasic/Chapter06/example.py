import sys
sys.path.append("C:/Pywork/DataScience/myCalcPackage")

# from myCalcPackage.calcModule import Add, Sub, Mul, Div

from calcModule import Add, Sub, Mul, Div

x = 10; y=5

print(f'Add={Add(x, y)}')
print(f'Sub={Sub(x, y)}')
print(f'Mul={Mul(x, y)}')
print(f'Div={Div(x, y)}')