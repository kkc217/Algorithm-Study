function solution(today, terms, privacies) {
    //tm = 약관 종류에 따른 유효기간을 쉽게 계산하기 위해 terms를 오브젝트로 변환
    //"A 1" => 'A':1
    let tm = terms.reduce((obj, term) => {
        let [key, val] = term.split(" ");
        obj[key] = Number(val);
        return obj;
    }, {});

    // privacy 또한 '1': ["YYYY.mm.dd", "A"] 형식으로 변환 함과 동시에
    //오브젝트 tm을 활용하여 '1': ["YYYY.mm.dd", "A"] => '1': ["YYYY.mm.dd", 1]로 약관 종류 A를 유효 기간 1로 변경
    let pri_Objs = privacies.reduce((obj, privacy, idx) => {
        let [key, val] = privacy.split(" ");
        obj[idx + 1] = [key, tm[val]];
        return obj;
    }, {});

    //개인정보 수집 일자 + 유효기간을 계산하여 배열로 변환 => [종료일1, 종료일2...]
    let pri_ends = Object.values(pri_Objs).map(([val1, val2]) => {
        let end = new Date(val1);
        end.setMonth(end.getMonth() + Number(val2));
        end.setDate(end.getDate());
        return end;
    });

    let answer = [];
    //td = 현재 날짜
    let td = new Date(today);

    //현재 날짜와 비교하여 종료일이 지난 개인정보들의 인덱스 추가
    pri_ends.forEach((v, i) => {
        if (v <= td) answer.push(i + 1);
    });

    return answer;
}

//result = [1, 3]
console.log(
    solution(
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    )
);

//result = [1, 4, 5]
console.log(
    solution(
        "2020.01.01",
        ["Z 3", "D 5"],
        [
            "2019.01.01 D",
            "2019.11.15 Z",
            "2019.08.02 D",
            "2019.07.01 D",
            "2018.12.28 Z",
        ]
    )
);
console.log(
    solution(
        "2020.01.01",
        ["A 1"],
        ["2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.01 A"]
    )
);

let obj = { A: 1, B: 2, C: 3 };

const entries = Object.entries(obj);
const keys = Object.keys(obj);
const values = Object.values(obj);

console.log(entries);
console.log(keys);
console.log(values);
