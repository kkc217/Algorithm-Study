import java.io.*;
import java.util.*;

public class Q1707 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int k = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for (int j = 0; j < k; j++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            HashMap<Integer, List<Integer>> map = new HashMap<>();
            for (int i = 1; i <= u; i++) {
                map.put(i, new ArrayList<>());
            }
            for (int i = 0; i < v; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                map.get(a).add(b);
                map.get(b).add(a);
            }

            boolean[] visited = new boolean[u + 1];
            Stack<Integer> stack = new Stack<>();
            boolean[] groups = new boolean[u + 1];
            boolean result = true;
            stack.push(1);
            visited[1] = true;
            while (!stack.isEmpty() && result) {
                while (!stack.isEmpty() && result) {
                    int current = stack.pop();
                    for (int node : map.get(current)) {
                        if (!visited[node]) {
                            groups[node] = !groups[current];
                            visited[node] = true;
                            stack.push(node);
                        } else if (groups[node] == groups[current]) {
                            result = false;
                            break;
                        }
                    }
                }
                for (int i = 1; i <= u; i++) {
                    if (!visited[i]) {
                        stack.push(i);
                        visited[i] = true;
                        break;
                    }
                }
            }
            if (result) bw.write("YES\n");
            else bw.write("NO\n");
        }

        bw.flush();
    }
}
