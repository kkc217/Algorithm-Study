function solution(n, m, section) {
    let cleared = 0;
    let paint = 0;
    for (let i of section) {
        if (i > cleared) {
            paint++;
            cleared = i + m - 1;
        }
    }
    return paint;
}
