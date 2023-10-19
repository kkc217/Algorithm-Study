import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q2263_kkc217 {
    static int n;
    static List<Integer> inorder = new ArrayList<>();
    static List<Integer> postorder = new ArrayList<>();
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            inorder.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            postorder.add(Integer.parseInt(st.nextToken()));
        }

        checkSubTree(0, n - 1, 0, n - 1);
        bw.flush();
    }

    static void checkSubTree(int inStart, int inEnd, int postStart, int postEnd) throws IOException {
        if (inStart > inEnd || postStart > postEnd) return;

        int rootValue = postorder.get(postEnd);
        bw.write(rootValue + " ");

        int inRootIndex = inorder.indexOf(rootValue);
        int leftLength = inRootIndex - inStart - 1;
        int rightLength = inEnd - inRootIndex - 1;

        checkSubTree(inStart, inRootIndex - 1, postStart, postStart + leftLength);
        checkSubTree(inRootIndex + 1, inEnd, postEnd - 1 - rightLength, postEnd - 1);
    }
}
