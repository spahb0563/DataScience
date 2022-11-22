#5. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(String)함수를 작성하라

def print_5xn(str) :
    for i in range(len(str)//5 + 1):
        start = i*5
        end = start+5
        print(str[start:end])


str = input("문자열을 입력해주세요 : ")

print_5xn(str)