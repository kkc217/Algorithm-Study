function solution(k, score) {
    let result = [];
    let dailyResult = [];
    for (let i = 0; i < k; i++) {
        dailyResult.push(score[i]);
        dailyResult.sort((a, b) => a - b);
        result.push(dailyResult[0]);

        if (i == score.length - 1) break;
    }

    for (let i = k; i < score.length; i++) {
        dailyResult.push(score[i]);
        dailyResult.sort((a, b) => b - a);
        result.push(dailyResult[k - 1]);
    }
    return result;
}

console.log(solution(10, [1, 10, 2, 5, 6, 7, 8]));
