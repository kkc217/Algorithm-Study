import java.io.*;
import java.util.StringTokenizer;

public class Q2629_kkc217 {
    static int n;
    static int[] weights;
    static boolean[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        weights = new int[n];
        dp = new boolean[n + 1][40001];
        for (int i = 0; i < n; i++) {
            weights[i] = Integer.parseInt(st.nextToken());
        }
        checkDP(0, 0);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            if (dp[n][target]) bw.write("Y ");
            else bw.write("N ");
        }
        bw.flush();
    }

    public static void checkDP(int idx, int weight) {
        if (dp[idx][weight]) return;
        dp[idx][weight] = true;
        if (idx == n) return;

        checkDP(idx + 1, weight);
        checkDP(idx + 1, weight + weights[idx]);
        checkDP(idx + 1, Math.abs(weight - weights[idx]));
    }
}
