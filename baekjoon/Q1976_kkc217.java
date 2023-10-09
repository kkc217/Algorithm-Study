import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q1976_kkc217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        boolean[][] routes = new boolean[n + 1][n + 1];
        StringTokenizer st;
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                routes[i][j] = Objects.equals(st.nextToken(), "1");
            }
        }

        int[] cities = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            cities[i] = Integer.parseInt(st.nextToken());
        }

        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(cities[0]);
        visited[cities[0]] = true;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int i = 1; i <= n; i++) {
                if (!visited[i] && routes[current][i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

        boolean result = true;
        for (int city : cities) {
            if (!visited[city]) {
                result = false;
                break;
            }
        }

        if (result) System.out.println("YES");
        else System.out.println("NO");
    }
}
