function solution(keymap, targets) {
    let result = [];

    for (let e of targets) {
        let sum = 0;
        for (let i = 0; i < e.length; i++) {
            let cnt = 101;
            for (let m of keymap) {
                if (m.indexOf(e[i]) == -1) {
                    continue;
                } else {
                    cnt = Math.min(cnt, m.indexOf(e[i]) + 1);
                }
            }
            if (cnt == 101) {
                sum = -1;
                break;
            } else {
                sum += cnt;
            }
        }
        result.push(sum);
    }
    return result;
}
