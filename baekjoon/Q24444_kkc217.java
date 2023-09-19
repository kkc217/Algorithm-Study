import java.io.*;
import java.util.*;

public class Q24444_kkc217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int[] visited = new int[n + 1];
        HashMap<Integer, List<Integer>> nodes = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            nodes.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            nodes.get(a).add(b);
            nodes.get(b).add(a);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(nodes.get(i));
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(r);
        int order = 1;
        while (!queue.isEmpty()) {
            if (visited[queue.peek()] != 0) {
                queue.poll();
                continue;
            }

            visited[queue.peek()] = order++;
            queue.addAll(nodes.get(queue.poll()));
        }

        for (int i = 1; i <= n; i++) {
            bw.write(visited[i] + "\n");
        }
        bw.flush();
    }
}
