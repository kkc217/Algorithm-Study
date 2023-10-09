import java.io.*;
import java.util.HashMap;
import java.util.Objects;
import java.util.StringTokenizer;

public class Q1991_kkc217 {
    static BufferedWriter bw;
    static HashMap<String, Node> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        map = new HashMap<>();

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            map.put(st.nextToken(), new Node(st.nextToken(), st.nextToken()));
        }

        preorder("A");
        bw.write("\n");
        inorder("A");
        bw.write("\n");
        postorder("A");

        bw.flush();
    }

    public static void preorder(String current) throws IOException {
        if (Objects.equals(current, ".")) return;

        bw.write(current);
        preorder(map.get(current).left);
        preorder(map.get(current).right);
    }

    public static void inorder(String current) throws IOException {
        if (Objects.equals(current, ".")) return;

        inorder(map.get(current).left);
        bw.write(current);
        inorder(map.get(current).right);
    }

    public static void postorder(String current) throws IOException {
        if (Objects.equals(current, ".")) return;

        postorder(map.get(current).left);
        postorder(map.get(current).right);
        bw.write(current);
    }

    static class Node {
        String left;
        String right;

        public Node(String left, String right) {
            this.left = left;
            this.right = right;
        }
    }
}
