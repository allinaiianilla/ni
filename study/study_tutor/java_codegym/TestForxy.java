public class TestForxy {
    public static void main(String[] args) {
        // 从 (1, 5) 开始，每轮同时移动两个对象
        for (int x = 1, y = 5; x <= 5; x++, y--) {
            System.out.println(x + " " + y);
        }
    }
}