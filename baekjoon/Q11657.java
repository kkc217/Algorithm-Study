import java.io.*;
import java.util.*;

public class Q11657 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Node>[] nodes = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int target = Integer.parseInt(st.nextToken());
            int distance = Integer.parseInt(st.nextToken());

            nodes[start].add(new Node(target, distance));
        }

        long[] distances = new long[n + 1];
        Arrays.fill(distances, Long.MAX_VALUE);
        distances[1] = 0;
        for (int j = 1; j < n; j++) {
            for (int i = 1; i <= n; i++) {
                for (Node node : nodes[i]) {
                    if (distances[i] == Long.MAX_VALUE) continue;
                    if (distances[node.target] > distances[i] + node.distance) {
                        distances[node.target] = distances[i] + node.distance;
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (Node node : nodes[i]) {
                if (distances[i] == Long.MAX_VALUE) continue;
                if (distances[node.target] > distances[i] + node.distance) {
                    System.out.println("-1");
                    return;
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            if (distances[i] == Long.MAX_VALUE) {
                bw.write("-1\n");
            } else {
                bw.write(distances[i] + "\n");
            }
        }
        bw.flush();
    }

    public static class Node {
        int target;
        int distance;

        public Node(int target, int distance) {
            this.target = target;
            this.distance = distance;
        }
    }
}
