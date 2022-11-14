multiline="""안녕하세요. 파이썬 세계로 온시걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

lines = []
words = []
for line in multiline.split('\n') :
    lines.append(line)
    for word in line.split() :
        words.append(word)

for word in words :
    print(word)
print(f'단어 개수 : {len(words)}')
