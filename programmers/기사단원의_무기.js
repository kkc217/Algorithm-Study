function solution(number, limit, power) {
    // 1 ~ number까지의 기사 번호 배열 생성
    const arr = new Array(number).fill(0).map((v, i) => (v = i + 1));

    //arr 원소들의 약수의 갯수 배열로 변환
    const divisor = arr.map((v) => {
        let cnt = 0;
        let a = Math.sqrt(v);
        for (let i = 1; i <= a; i++) {
            if (v % i === 0) cnt += 2;
        }
        if (a === Math.round(a)) cnt--;
        return cnt;
    });

    // limit을 넘는 원소를 power로 변경 후 합산
    const atk_power = divisor.map((v) => {
        if (v > limit) v = power;
        return v;
    });

    return atk_power.reduce((a, c) => a + c);
}

console.log(solution(10, 3, 2));
