public class TestWhile {
    public static void main(String[] args){
        // 打印一百次你好 
        int i = 1;
        while (i <= 100){
            String message = "第" + i + "次: 你好";
            System.out.println(message);
            i = i + 1;
        }
    }
}
