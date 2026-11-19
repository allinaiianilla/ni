public class TestStringParse {
    public static void main(String[] args) {
        int a = 10; // 声明一个整型变量 a，并赋值为 10
        String str2 = String.valueOf(a); // 将整型变量 a 转换为字符串，并赋值给 str2
        String str3 = "123"; // 声明一个字符串变量 str3，并赋值为 "123"
        int b = Integer.parseInt(str3); // 将字符串 str3 转换为整型，并赋值给 b
        System.out.println("b = " + b);
    }
}
