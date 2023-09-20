function solution(s, skip, index) {
    let apb = "abcdefghijklmnopqrstuvwxyz";
    apb = apb.split("");
    skip = skip.split("");

    for (const x of skip) {
        apb.splice(apb.indexOf(x), 1);
    }

    return [...s]
        .map(
            (v) =>
                apb[apb.indexOf(v) + index] ||
                apb[apb.indexOf(v) + index - apb.length] ||
                apb[apb.indexOf(v) + index - apb.length * 2]
        )
        .join("");
}
