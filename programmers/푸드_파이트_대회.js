function solution(food) {
    let set = [];
    //좌우 대칭으로 배치해야 하므로, (음식의 갯수 / 2)를 정수부분까지 버린 후 one-side에 배치
    food.forEach((e, i) => {
        if (i == 0) {
        } else {
            set.push(`${i}`.repeat(Math.floor(e / 2)));
        }
    });
    // 반대편에 뒤집어 배치할 배열 형성, reverse()는 기존의 배열을 뒤집으므로 스프레드 연산자로 새 배열 생성 후 reverse
    let reversed = [...set].reverse();
    // 0 (물) 삽입
    set.push(0);
    //반대편 음식 배치
    set.push(...reversed);
    //어레이 -> 스트링으로 병합
    return set.join("");
}

console.log(solution([1, 3, 4, 6]));
