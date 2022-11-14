while True:
    height = int(input('홀수를 입력하세요(0 <- 종료)'))

    if height == 0:
        print('마름모 프로그램 출력을 이용해 주셔서 감사합니다.')
        break
    elif height < 0 or height % 2 == 0:
        print('입력 오류')
        continue

    middle = height // 2;
    for i in range(height) :
        start = abs(middle - i)
        if i > middle :
            end -= 1
        else :
            end = middle + i;
        for j in range(height) :
            if start <= j <= end:
                print('*', end='')
            else :
                print(' ', end='')
        print()