word = input()
len = len(word)
Palindrome = False
if len == 1:
    Palindrome = True
for i in range(len//2):
    if word[i] != word[len - 1 - i]:
        Palindrome = False
        break
    else:
        Palindrome = True

if Palindrome:
    print("1")
else:
    print("0")