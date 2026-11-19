public class TestString {
    public static void main(String[] args) {
        String str1 = "Hello"; // 声明一个字符串变量 str1，并赋值为 "Hello"
        String str2 = "World"; // 声明一个字符串变量 str2，并赋值为 "World"
        String str3 = str1 + " " + str2; // 字符串拼接
        System.out.println(str3);
        String str4 = "Java"; // 声明一个字符串变量 str4，并赋值为 "Java"
        String str5 = "CodeGym"; // 声明一个字符串变量 str5，并赋值为 "CodeGym"
        String str6 = str4.toLowerCase() + " " + str5.toUpperCase(); // 字符串转换为小写和大写
        System.out.println(str6);
        String str7 = "  Java CodeGym  "; // 声明一个字符串变量 str7，并赋值为 "  Java CodeGym  "
        System.out.println("start" + str7 + "end");
        String str8 = str7.trim(); // 去除字符串前后的空格
        System.out.println("start" + str8 + "end");
    }
}