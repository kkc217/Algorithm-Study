import java.util.*;

public class 표_병합_kkc217 {
    public static int MAX_SIZE = 51;

    public static String[] solution(String[] commands) {
        List<String> answer = new ArrayList<>();
        Cell[][] matrix = new Cell[MAX_SIZE][MAX_SIZE];
        for (int i = 1; i < MAX_SIZE; i++) {
            for (int j = 1; j < MAX_SIZE; j++) {
                matrix[i][j] = new Cell(null);
            }
        }

        for (String command : commands) {
            String[] inputs = command.split(" ");

            switch (inputs[0]) {
                case "UPDATE":
                    if (inputs.length == 4) {
                        int r = Integer.parseInt(inputs[1]);
                        int c = Integer.parseInt(inputs[2]);

                        matrix[r][c].getParent().value = inputs[3];
                    } else {
                        for (int i = 1; i < MAX_SIZE; i++) {
                            for (int j = 1; j < MAX_SIZE; j++) {
                                Cell cell = matrix[i][j].getParent();
                                if (Objects.equals(inputs[1], cell.value)) {
                                    cell.value = inputs[2];
                                }
                            }
                        }
                    }
                    break;
                case "MERGE":
                    int r1 = Integer.parseInt(inputs[1]);
                    int c1 = Integer.parseInt(inputs[2]);
                    int r2 = Integer.parseInt(inputs[3]);
                    int c2 = Integer.parseInt(inputs[4]);

                    Cell parent1 = matrix[r1][c1].getParent();
                    Cell child1 = matrix[r1][c1].getChild();
                    Cell parent2 = matrix[r2][c2].getParent();
                    if (Objects.equals(parent1, parent2)) break;

                    if (Objects.isNull(parent1.value))
                        parent1.value = parent2.value;

                    parent2.parent = child1;
                    child1.child = parent2;
                    break;
                case "UNMERGE":
                    int r = Integer.parseInt(inputs[1]);
                    int c = Integer.parseInt(inputs[2]);

                    Cell current = matrix[r][c].getParent();
                    String value = current.value;
                    current.value = null;
                    while (Objects.nonNull(current.child)) {
                        Cell child = current.child;
                        current.child = null;

                        child.value = null;
                        child.parent = null;

                        current = child;
                    }

                    matrix[r][c].value = value;
                    break;
                case "PRINT":
                    String printValue = matrix[Integer.parseInt(inputs[1])][Integer.parseInt(inputs[2])].getParent().value;
                    if (Objects.isNull(printValue)) {
                        answer.add("EMPTY");
                    } else {
                        answer.add(printValue);
                    }
                    break;
            }
        }

        return answer.toArray(new String[0]);
    }

    static class Cell {
        Cell child;
        Cell parent;
        String value;

        public Cell(String value) {
            this.value = value;
        }

        public Cell getParent() {
            if (Objects.nonNull(parent)) {
                return parent.getParent();
            }
            return this;
        }

        public Cell getChild() {
            if (Objects.nonNull(child)) {
                return child.getChild();
            }
            return this;
        }
    }

    public static void main(String[] args) {
//        String[] commands = {"UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"};
//        String[] result = solution(commands);
//        String[] commands = {"UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"};
//        String[] result = solution(commands);
        String[] commands = {"MERGE 1 1 1 2", "UPDATE 1 1 kk", "MERGE 1 2 1 1", "PRINT 1 1", "PRINT 1 2"};
        String[] result = solution(commands);
        System.out.println(Arrays.toString(result));
    }
}
