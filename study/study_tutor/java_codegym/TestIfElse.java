public class TestIfElse {
    public static void main(String[] args) {

        // 1. if else 通过条件语句的执行情况来决定执行哪一个代码块
        // 2. 语句块 包含多条语句,用大括号包裹

        int a = 10; // 声明一个整型变量 a，并赋值为 10
        int b = 20; // 声明一个整型变量 b，并赋值为 20
        if (a > b) { // 判断 a 是否大于 b
            // 条件语句为真执行该代码块
            System.out.println("a 大于 b");
        } else if (a < b) { // 判断 a 是否小于 b
            // 条件语句为真执行该代码块
            System.out.println("a 小于 b");
        } else {
            // 上面条件语句都不为真执行该代码块
            System.out.println("a 等于 b");
        }
    }
}
