public class 미로_탈출_명령어_kkc217 {
    public static String solution(int n, int m, int x, int y, int r, int c, int k) {
        String[][] matrix = new String[n + 1][m + 1];
        matrix[x][y] = "";

        for (int cnt = 1; cnt <= k; cnt++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    if (matrix[i][j] != null && matrix[i][j].length() == cnt - 1) {
                        if (i > 1 && (
                                matrix[i - 1][j] == null ||
                                matrix[i - 1][j].length() != cnt ||
                                matrix[i - 1][j].compareTo(matrix[i][j]) > 0
                        )) matrix[i - 1][j] = matrix[i][j] + "u";
                        if (i < n && (
                                matrix[i + 1][j] == null ||
                                matrix[i + 1][j].length() != cnt ||
                                matrix[i + 1][j].compareTo(matrix[i][j]) > 0
                        )) matrix[i + 1][j] = matrix[i][j] + "d";
                        if (j > 1 && (
                                matrix[i][j - 1] == null ||
                                matrix[i][j - 1].length() != cnt ||
                                matrix[i][j - 1].compareTo(matrix[i][j]) > 0
                        )) matrix[i][j - 1] = matrix[i][j] + "l";
                        if (j < m && (
                                matrix[i][j + 1] == null ||
                                matrix[i][j + 1].length() != cnt ||
                                matrix[i][j + 1].compareTo(matrix[i][j]) > 0
                        )) matrix[i][j + 1] = matrix[i][j] + "r";
                    }
                }
            }
        }

        if (matrix[r][c] != null && matrix[r][c].length() == k) return matrix[r][c];
        else return "impossible";
    }

    public static void main(String[] args) {
//        String result = solution(3, 4, 2, 3, 3, 1, 5); // dllrl
//        String result = solution(2, 2, 1, 1, 2, 2, 2); // dr
        String result = solution(3, 3, 1, 2, 3, 3, 4); // impossible
        System.out.println(result);
    }
}
