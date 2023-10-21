import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q11723_kkc217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int m = Integer.parseInt(br.readLine());
        boolean[] sets = new boolean[21];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "all":
                    Arrays.fill(sets, true);
                    continue;
                case "empty":
                    Arrays.fill(sets, false);
                    continue;
            }

            int num = Integer.parseInt(st.nextToken());
            switch (command) {
                case "add":
                    sets[num] = true;
                    break;
                case "remove":
                    sets[num] = false;
                    break;
                case "check":
                    if (sets[num]) bw.write("1\n");
                    else bw.write("0\n");
                    break;
                case "toggle":
                    sets[num] = !sets[num];

            }
        }

        bw.flush();
    }
}
