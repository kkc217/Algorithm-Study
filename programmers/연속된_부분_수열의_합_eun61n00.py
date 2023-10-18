def solution(sequence, k):
    answers = []
    
    sum = 0
    l, r = 0, 0
    sum = sequence[0]
    
    if sum == k:
        return [0, 0]
    
    while True:
            
        if sum < k: # 오른쪽으로 한 칸 이동(더하기)
            if r >= len(sequence) - 1:
                break
            r += 1
            sum += sequence[r]

        else: # 왼쪽 빼기
            if l >= len(sequence) - 1:
                break
            sum -= sequence[l]
            l += 1
        
        if sum == k: # sum과 k가 같음
            answers.append((l, r))
        
    answers.sort(key = lambda x: ((x[1] - x[0]), x[0]))
    
    return answers[0]
