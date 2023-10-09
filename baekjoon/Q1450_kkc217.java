import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q1450_kkc217 {

    static int n, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        List<Integer> weights1 = new ArrayList<>();
        List<Integer> weights2 = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            if (i < n / 2) weights1.add(Integer.parseInt(st.nextToken()));
            else weights2.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> sum1 = new ArrayList<>();
        List<Integer> sum2 = new ArrayList<>();

        dfs(0, 0, weights1, sum1);
        dfs(0, 0, weights2, sum2);

        Collections.sort(sum2);
        int answer = 0;
        for (int i = 0; i < sum1.size(); i++) {
            int weight = c - sum1.get(i);
            answer += binarySearch(sum2, weight) + 1;
        }

        System.out.println(answer);
    }

    public static void dfs(int idx, int sum, List<Integer> weights, List<Integer> answer) {
        if (sum > c) return;
        if (idx == weights.size()) {
            answer.add(sum);
            return;
        }

        dfs(idx + 1, sum + weights.get(idx), weights, answer);
        dfs(idx + 1, sum, weights, answer);
    }

    public static int binarySearch(List<Integer> sum, int target) {
        int left = 0;
        int right = sum.size() - 1;
        int mid;
        int answer = -1;

        while (left <= right) {
            mid = (left + right) / 2;
            if (sum.get(mid) <= target) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }
}
