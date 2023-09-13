import java.io.*;
import java.util.*;

public class Q9370 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;
        while (T > 0) {
            T--;
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            List<Node>[] nodes = new ArrayList[n + 1];
            for (int i = 0; i <= n; i++) {
                nodes[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());

                if ((a == g && b == h) || (a == h && b == g)) {
                    nodes[a].add(new Node(b, d, true));
                    nodes[b].add(new Node(a, d, true));
                } else {
                    nodes[a].add(new Node(b, d, false));
                    nodes[b].add(new Node(a, d, false));
                }
            }

            int[] distances = new int[n + 1];
            Arrays.fill(distances, Integer.MAX_VALUE);
            boolean[] checks = new boolean[n + 1];
            Queue<Integer> queue = new LinkedList<>();

            queue.add(s);
            distances[s] = 0;
            while (!queue.isEmpty()) {
                int current = queue.poll();
                for (Node node : nodes[current]) {
                    if (distances[current] + node.distance < distances[node.target]) {
                        distances[node.target] = distances[current] + node.distance;
                        checks[node.target] = node.check || checks[current];
                        queue.add(node.target);
                    } else if (distances[current] + node.distance == distances[node.target]) {
                        if (!checks[node.target] && (checks[current] || node.check)) {
                            checks[node.target] = true;
                            queue.add(node.target);
                        }
                    }
                }
            }

            List<Integer> result = new ArrayList<>();
            for (int i = 0; i < t; i++) {
                int idx = Integer.parseInt(br.readLine());
                if (checks[idx]) {
                    result.add(idx);
                }
            }

            Collections.sort(result);
            for (int idx : result) {
                bw.write(idx + " ");
            }
            bw.write("\n");
        }
        bw.flush();
    }

    static class Node {
        int target;
        int distance;
        boolean check;

        Node(int target, int distance, boolean check) {
            this.target = target;
            this.distance = distance;
            this.check = check;
        }
    }
}
