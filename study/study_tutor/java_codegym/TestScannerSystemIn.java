public class TestScannerSystemIn {
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in); // 创建一个 Scanner 对象，用于从控制台读取输入
        System.out.print("请输入一个整数: "); // 提示用户输入一个整数
        int num = scanner.nextInt(); // 读取用户输入的整数，并赋值给变量 num; nextInt() 方法会读取整数，但不会消耗换行符
        System.out.println("您输入的整数是: " + num); // 输出用户输入的整数

        // 消耗掉换行符，避免影响下一次读取
        scanner.nextLine(); // 读取并丢弃换行符

        System.out.print("请输入一个字符串: "); // 提示用户输入一个字符串
        String str = scanner.nextLine(); // 读取用户输入的字符串，并赋值给变量 str
        System.out.println("您输入的字符串是: " + str); // 输出用户

        scanner.close(); // 关闭 Scanner 对象，释放资源
    }
}
