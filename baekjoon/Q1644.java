import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Q1644 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> primes = new ArrayList<>();
        boolean[] checks = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            if (!checks[i]) {
                primes.add(i);
            }
            int current = 2;
            while (i * current <= n) {
                checks[i * current] = true;
                current++;
            }
        }

        int start = 0;
        int end = 0;
        int result = 0;
        int sum = 0;
        if (primes.size() > 0) sum = primes.get(0);
        while (end < primes.size()) {
            if (sum == n) {
                result++;
            }
            if (sum <= n) {
                end++;
                if (end < primes.size()) sum += primes.get(end);
            } else {
                sum -= primes.get(start);
                start++;
            }
        }

        System.out.println(result);
    }
}
