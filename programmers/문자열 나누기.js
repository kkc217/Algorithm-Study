function solution(s) {
    let s_arr = [];
    let first_letter_count = 0;
    let else_letter_count = 0;
    let first_letter = "";

    // 빈 배열을 만들어서 s의 요소를 하나씩 삽입하다가 분해 될 때마다 구분자 '-' 넣어주기
    for (let letter of s) {
        if (first_letter == "") {
            first_letter = letter;
            first_letter_count++;
            s_arr.push(letter);
        } else {
            letter == first_letter ? first_letter_count++ : else_letter_count++;
            s_arr.push(letter);
            if (first_letter_count === else_letter_count) {
                s_arr.push("-");
                first_letter_count = 0;
                else_letter_count = 0;
                first_letter = "";
            }
        }
    }

    //구분자로 구분되는 배열로 재배열시 마지막 요소가 '-'로 끝나는 경우 '-'빼주기
    let answer = s_arr.join("").split("-");
    if (answer[answer.length - 1] == "") answer.pop();
    return answer.length;
}

console.log(solution("banana"));
