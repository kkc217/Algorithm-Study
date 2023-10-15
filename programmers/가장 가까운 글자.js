function solution(s) {
    return [...s].map((compVal, idx) => {
        return [...s.slice(0, idx)].lastIndexOf(compVal) + 1
            ? idx - [...s.slice(0, idx)].lastIndexOf(compVal)
            : -1;
    });
}

console.log(solution("banana"));
