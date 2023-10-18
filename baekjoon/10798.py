word_array = [["*" for i in range(15)]for i in range(5)]  # 15개의 *을 가지는 리스트를 5개 생성
max_line = 0
for i in range(5):
    word_line = input()
    if len(word_line) > max_line:
        max_line = len(word_line)
    for j in range(len(word_line)):
        word_array[i][j] = word_line[j]

for j in range(max_line):
    for i in range(5):
        if word_array[i][j] == "*":
            continue
        else:
            print(word_array[i][j], end="")