import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q13549 {
    public static void main(String[] args) throws IOException {
        final int MAX = 100000;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] result = new int[MAX + 1];
        Arrays.fill(result, MAX + 1);
        result[n] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);
        while (!queue.isEmpty()) {
            Integer current = queue.poll();
            if (current != 0 && current * 2 <= MAX && result[current] < result[current * 2]) {
                result[current * 2] = result[current];
                if (result[current] < result[k])
                    queue.add(current * 2);
            }

            if (current > 0 && result[current] + 1 < result[current - 1]) {
                result[current - 1] = result[current] + 1;
                if (result[current] + 1 < result[k])
                    queue.add(current - 1);
            }

            if (current < MAX && result[current] + 1 < result[current + 1]) {
                result[current + 1] = result[current] + 1;
                if (result[current] + 1 < result[k])
                    queue.add(current + 1);
            }
        }

        System.out.println(result[k]);
    }
}
