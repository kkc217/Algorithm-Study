def solution(arr1, arr2):
    answer = []
    for i in arr1:
        item = []
        for col in range(len(arr2[0])):
            sum = 0
            for row, num in enumerate(i):
                sum += num * arr2[row][col]
            item.append(sum)
        answer.append(item)
    return answer