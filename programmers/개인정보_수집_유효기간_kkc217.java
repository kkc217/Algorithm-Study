import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) throws ParseException {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy.MM.dd");
        Date todayDate = dateFormat.parse(today);
        Calendar calendar = Calendar.getInstance();

        HashMap<String, Date> map = new HashMap<>();
        for (String term : terms) {
            String[] termArr = term.split(" ");
            calendar.setTime(todayDate);
            calendar.add(Calendar.MONTH, -Integer.parseInt(termArr[1]));
            map.put(termArr[0], calendar.getTime());
        }

        List<Integer> result = new ArrayList<>();
        for (int idx = 0; idx < privacies.length; idx++) {
            String[] privacyArr = privacies[idx].split(" ");
            if (!map.get(privacyArr[1]).before(dateFormat.parse(privacyArr[0]))) {
                result.add(idx + 1);
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) throws ParseException {
        Solution solution = new Solution();
        String today = "2022.05.19";
        String[] terms = {"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
//        String today = "2020.01.01";
//        String[] terms = {"Z 3", "D 5"};
//        String[] privacies = {"2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"};
        int[] result = solution.solution(today, terms, privacies);
        System.out.println(Arrays.toString(result));
    }
}
