public class TestDoWhile {
    public static void main(String[] args) {
        int i = 1000; // 初始化计数器 i 为 1
        do {
            String message = "第" + i + "次: 你好"; // 构建输出消息
            System.out.println(message); // 输出消息到控制台
            i++; // 计数器自增
        } while (i <= 100); // 当计数器小于等于 100 时继续循环
    }
}
