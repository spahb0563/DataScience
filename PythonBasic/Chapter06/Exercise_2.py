from math import sqrt
from statistics import mean

#[문제2]

class Scattering:

    def __init__(self, lst):
        self.lst = lst

    def var_func(self):

        average = mean(self.lst)

        diff = [(i-average)**2 for i in self.lst]

        self.var = sum(diff) / (len(self.lst)-1)

        return self.var
    def std_func(self):

        std = sqrt(self.var)

        return std

x = [5, 9, 1, 7, 4, 6]

scattering =  Scattering(x)

print(f'분산 : {scattering.var_func()}')

print(f'표준편차 : {scattering.std_func()}')