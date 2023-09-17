function solution(t, p) {
    return (
        //t를 배열로 만든 후 reduce 사용
        [...t].reduce(
            //누산값과 인덱스를 활용
            (acc, cur, idx) =>
                (acc =
                    acc +
                    //인덱스를 순회하며 슬라이싱할 위치 지정 => t 슬라이스
                    //조건에 맞는 부분문자열만 누산값에 값추가
                    (+t.slice(idx, idx + p.length) <= +p ? 1 : 0)),
            0
        ) -
        //배열을 전체 순회하는 reduce의 특성 상 p보다 자릿수가 작은 t의 부분 문자열은 항상 p보다 작으므로,
        //문제에서 요구하는 결과 값보다 p.length -1 만큼 크다.
        (p.length - 1)
    );
}

console.log(solution("3141592", "271"));
