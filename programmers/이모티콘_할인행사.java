import java.util.Arrays;

public class 이모티콘_할인행사 {
    public static int maxSubscriber = 0;
    public static int maxPrice = 0;

    public static int[] solution(int[][] users, int[] emoticons) {
        int[] discountPercents = {10, 20, 30, 40};

        int[] discounts = new int[emoticons.length];
        recursion(discounts, 0, emoticons, discountPercents, users);

        int[] answer = {maxSubscriber, maxPrice};
        return answer;
    }

    public static void recursion(int[] discounts, int depth, int[] emotions, int[] discountPercents, int[][] users) {
        if (depth != emotions.length) {
            for (int i = 0; i < discountPercents.length; i++) {
                discounts[depth] = discountPercents[i];
                recursion(discounts, depth + 1, emotions, discountPercents, users);
            }
        } else {
            int subscribers = 0;
            int totalPrice = 0;
            int[] userTotal = new int[users.length];
            for (int i = 0; i < userTotal.length; i++) {
                for (int j = 0; j < discounts.length; j++) {
                    if (discounts[j] >= users[i][0]) {
                        userTotal[i] += emotions[j] * (100 - discounts[j]) / 100;
                    }
                }
                if (userTotal[i] >= users[i][1]) {
                    subscribers++;
                } else {
                    totalPrice += userTotal[i];
                }
            }

            if (maxSubscriber < subscribers) {
                maxSubscriber = subscribers;
                maxPrice = totalPrice;
            } else if (maxSubscriber == subscribers && maxPrice < totalPrice) {
                maxPrice = totalPrice;
            }
        }
    }

    public static void main(String[] args) {
//        int[][] users = {{40, 10000}, {25, 10000}};
//        int[] emotions = {7000, 9000};
        int[][] users = {{40, 2900}, {23, 10000}, {11, 5200}, {5, 5900}, {40, 3100}, {27, 9200}, {32, 6900}};
        int[] emotions = {1300, 1500, 1600, 4900};
        int[] result = solution(users, emotions);
        System.out.println(Arrays.toString(result));
    }
}
