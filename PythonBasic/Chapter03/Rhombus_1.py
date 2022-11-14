while True :
    base = int(input('홀수를 입력하세요(0 <- 종료)'))

    if base == 0 :
        print('마름모 프로그램 출력을 이용해 주셔서 감사합니다.')
        break
    elif base < 0 or base % 2 == 0 :
        print('입력 오류')
        continue

    height = int((base+1)/2)

    for i in range(height) :
        for j in range(height-i-1) :
            print(' ', end='')
        for j in range(2*i+1) :
            print('*', end='')
        print()
