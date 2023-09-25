function solution(k, m, score) {
    //소팅
    const sortedScore = score.sort((a, b) => a - b);

    //한 박스에 들어가는 과일의 수에 맞춰서  포장 불가능한 과일 제거
    const remains = sortedScore.length % m;
    sortedScore.splice(0, remains);

    //m 간격으로 포장 할 것이므로 박스의 최솟값 sortedScore[i] * 박스에 담기는 과일의 수 m 를 합산하여 리턴
    let result = 0;
    for (let i = 0; i < sortedScore.length; i += m) {
        result += sortedScore[i] * m;
    }

    return result;
}

console.log(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]));
