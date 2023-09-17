public class 택배_배달과_수거하기 {
    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
        int deliveryTemp = 0;
        int pickupTemp = 0;
        long answer = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (deliveries[i] != 0 || pickups[i] != 0) {
                int cnt = 0;
                while (deliveryTemp < deliveries[i] || pickupTemp < pickups[i]) {
                    cnt++;
                    deliveryTemp += cap;
                    pickupTemp += cap;
                }
                deliveryTemp -= deliveries[i];
                pickupTemp -= pickups[i];
                answer += (long) (i + 1) * cnt * 2;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int cap = 4;
        int n = 5;
        int[] deliveries = {1, 0, 3, 1, 2};
        int[] pickups = {0, 3, 0, 4, 0};
//        int cap = 2;
//        int n = 7;
//        int[] deliveries = {1, 0, 2, 0, 1, 0, 2};
//        int[] pickups = {0, 2, 0, 1, 0, 2, 0};

        long result = solution(cap, n, deliveries, pickups);
        System.out.println(result);
    }
}
