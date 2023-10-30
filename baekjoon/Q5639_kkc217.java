import java.io.*;

public class Q5639_kkc217 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        Node root = new Node(Integer.parseInt(br.readLine()));
        String input = br.readLine();
        while (input != null && !input.equals("")) {
            addNode(Integer.parseInt(input), root);

            input = br.readLine();
        }

        postOrder(root);
        bw.flush();
    }

    public static void addNode(int value, Node node) {
        if (value > node.value) {
            if (node.right == null) {
                node.right = new Node(value);
            } else {
                addNode(value, node.right);
            }
        } else {
            if (node.left == null) {
                node.left = new Node(value);
            } else {
                addNode(value, node.left);
            }
        }
    }

    public static void postOrder(Node node) throws IOException {
        if (node == null) return;

        postOrder(node.left);
        postOrder(node.right);
        bw.write(node.value + "\n");
    }

    static class Node {
        int value;
        Node left;
        Node right;

        Node(int value) {
            this.value = value;
        }
    }
}
