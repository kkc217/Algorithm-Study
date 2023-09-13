import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Q10815_kkc217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(Integer.parseInt(st.nextToken()), 0);
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int result = map.containsKey(Integer.parseInt(st.nextToken())) ? 1 : 0;
            bw.write(result + " ");
        }

        bw.flush();
    }
}
