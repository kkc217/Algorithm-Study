N = int(input())

continuous_word = 0

for i in range(N):
    is_continue = False
    word = input()
    for j in range(len(word) - 1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                is_continue = False
                break
            else:
                is_continue = True
        else:
            is_continue = True
    if is_continue or len(word) == 1:
        continuous_word += 1
print(continuous_word)