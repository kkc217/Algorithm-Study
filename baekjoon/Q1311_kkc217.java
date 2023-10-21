import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q1311_kkc217 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] costs = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                costs[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] dp = new int[n + 1][(1 << n)];
        for (int i = 0; i <= n; i++) {
            int[] row = new int[(1 << n)];
            Arrays.fill(row, Integer.MAX_VALUE);
            dp[i] = row;
        }
        dp[0][0] = 0;

        for (int person = 1; person <= n; person++) {
            for (int dpIndex = 0; dpIndex < (1 << n); dpIndex++) {
                for (int work = 1; work <= n; work++) {
                    int workBitNum = 1 << (work - 1);
                    if (dp[person - 1][dpIndex] != Integer.MAX_VALUE &&
                            (dpIndex & workBitNum) == 0) {
                        dp[person][dpIndex | workBitNum] = Math.min(dp[person][dpIndex | workBitNum], dp[person - 1][dpIndex] + costs[person][work]);
                    }
                }
            }
        }

        System.out.println(dp[n][(1 << n) - 1]);
    }
}
