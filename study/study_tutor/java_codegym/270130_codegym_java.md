# codegym_java_270201

> 学习编程语言有两条路径,一个是按部就班的跟着教程学习, 这个是非常棒的,可以系统的学习到知识,只是过程可能乏味,大多情况会中途放弃!当然,我已经中途放弃过很多教程. 第二条路径是根据诉求或需求或实现来学习, 这个路径的好处就是直达目标,直击核心,坏处就是不系统,无计划,如果没有坚定的信念,也会很快半途而废,比第一种还容易. 因为你没有计划甚至没有第二天的学习目标和计划.

> 现在就开始第一条路径的学习.
> 不是单纯的学习,而是把教程学习的这条路打通. 每天进行,有目标.完成目标.完成最终的学习目标.



> 废话不多说了, 开始!**完成目标**

## 基础知识

### 级别一 命令与第一个Java程序

#### 命令与第一个java程序

1. 理解程序

> 程序: 用户要给计算机下达的一系列命令
> 运行程序: 计算机执行用户下达的命令


不要把程序员想象成某种不可思议的东西, 他只是给计算机下达一个命令或一系列命令.计算机就会根据命令来工作.  

这些命令都具备特定的规则,否则计算机听不懂.仅此而已.


> 程序就是一组（列表）命令。先执行第一条命令，然后第二条、第三条，依此类推。当所有命令执行完，程序就结束。
> java语言的命令集合非常丰富

示例:  
`System.out.println("first command");`
`System.out.println("Second command");`

2. java程序规则

> 把第一个要执行的命令放到mian方法中
> main方法中放第一个要执行的命令

* main() 方法, java程序会找到main方法,然后从main方法开始依次执行方法

```java
void main() 
    {
        // 方法中的命令
        // 输出短语 "做程序员很酷！😎"
        System.out.println("大家好！");
        System.out.println("今天我们来学习如何用Java 编程！");
        System.out.println("做程序员很酷！😎");
    }
```


#### java中的屏幕输出: System.out.println 与 System.out.print

> 任何java程序都由一条条命令组成.
> 每条命令的末尾都要加上分号

```java
public class TestPrint {
    public static void main(String[] args){
        System.out.println("会换行");
        System.out.println("会换行");
        System.out.print("不会换行");
        System.out.print("不会换行");

    }
}
```

#### 认识变量

1. 变量与盒子

变量 是一种用于存储数据的特殊的容器.

变量的三个属性
* 类型
* 名称
* 值

2. 创建变量

`type name;`

示例:
* int a; // 声明一个整数类型的变量,变量名是a
* String s;
* double c;

3. 赋值

把值放入变量 -- 赋值

`name = value;`

示例:
* a = 1;
* s = "njh";
* a = a + 1;

4. 变量名

* 英文
* 下划线
* 数字

```java
public class TestBianliang {
    public static void main(String[] args) {
        int a = 10; // 声明一个整型变量 a，并赋值为 10
        int b = 20; // 声明一个整型变量 b，并赋值为 20
        int c = a + b; // 声明一个整型变量 c，并赋值为 a 和 b 的和
        System.out.println("a + b = " + c);
    }
}
```


#### 变量类型

1. 变量声明

`类型 名称;`

* int 整数
* String 字符串

2. int类型

* 类型: 整数
* 操作: 可以进行算术运算; +-*/ 加减乘除

3. String类型

* 类型: 用于存储文本字符串
* 规则: 文本两侧加上双引号
* 操作
    1. 字符串拼接 `String s1 = "a" + "b"` // "ab"
   
```java
public class TestBianliangCaozuo {
    public static void main(String[] args) {
        int a = 10; // 声明一个整型变量 a，并赋值为 10
        int b = 20; // 声明一个整型变量 b，并赋值为 20
        int c = a + b; // 声明一个整型变量 c，并赋值为 a 和 b 的和
        System.out.println("a + b = " + c);
        String str1 = "Hello"; // 声明一个字符串变量 str1，并赋值为 "Hello"
        String str2 = "World"; // 声明一个字符串变量 str2，并赋值为 "World"
        String str3 = str1 + " " + str2; // 字符串拼接
        System.out.println(str3);
    }
}
```


#### 编译器与注释

##### 编译
> 命令写好了, 如何运行呢?
1. 新建文本文件,后缀.java,编写要执行的命令
2. 使用javac编译命令,将文本文件编译生成一个字节码文件
3. 使用java命令,调用java虚拟机执行字节码文件

##### 注释
> 对代码的解释,不会被当成命令执行
`int a = 5; // 声明一个整数类型变量a, 并给a赋值5`
```java
/*
    多行注释 第一行
    多行注释 第二行
*/
```

### 级别二 整数：int 类型，int 类型的运算

#### 整数：int 类型，int 类型的运算

> int Integer的缩写,英文整数
> int 类型的大小,占4个字节(每个字节8比特,总计32位比特), 整数范围大约是 -20亿 到 +20亿


```java
public class TestInt {
    public static void main(String[] args) {
        int a = 10; // 声明一个整型变量 a，并赋值为 10
        int b = 20; // 声明一个整型变量 b，并赋值为 20
        int c = a + b; // 声明一个整型变量 c，并赋值为 a 和 b 的和
        System.out.println("a + b = " + c);
        int d = a * b; // 声明一个整型变量 d，并赋值为 a 和 b 的积
        System.out.println("a * b = " + d);
        int e = b - a; // 声明一个整型变量 e，并赋值为 b 和 a 的差
        System.out.println("b - a = " + e);
        int f = b / a; // 声明一个整型变量 f，并赋值为 b 和 a 的商
        System.out.println("b / a = " + f);
        int g = b % a; // 声明一个整型变量 g，并赋值为 b 和 a 的余数
        System.out.println("b % a = " + g);
    }
}
```

#### 字符串与文本：String 类型，字符串操作

1. 存储内容: 字符串
2. 表示方式: 使用双引号包裹
3. 表示方式: 反斜杠是转义符, `\n` 表示换行符
4. 操作方式:
    1. 拼接字符串, 两个字符串相加 `"aa" + " " + "bb"`
    2. 字符串内置方法-(类似System.out.println()的函数,只是基于字符串才有函数,叫方法)-使用方法`变量.方法()`
        * length() 字符串长度 `"aaa".length()` 3
        * toUpperCase() 转为大写
        * toLowerCase() 转为小写
        * trim() 两边去空格
```java
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
```

#### 数据类型之间的转换

1. 为什么需要类型转换?
> java是一种强类型语言.不能往变量中放其他类型数据.
> 如需要转换变量数据类型,需要显性进行转换

2. 将 int 转换为 String

> `String.valueOf()`会把传入对象的值转会为字符串类型

3. 隐式转换为字符串

> java的设计使得在java中几乎所有变量,对象,表达式都可以转换为string
> 当我们把String类型数据与其他类型相加时,这种转换就会自动发生

```java
int a = 5;
String name = "Anya" + a;
```

> 不能对 String 类型执行算术运算.即便该字符串完全由数字组成

4. 将字符串转换为数字

`Integer.parseInt(string)`

```java
public class TestStringParse {
    public static void main(String[] args) {
        int a = 10; // 声明一个整型变量 a，并赋值为 10
        String str2 = String.valueOf(a); // 将整型变量 a 转换为字符串，并赋值给 str2
        String str3 = "123"; // 声明一个字符串变量 str3，并赋值为 "123"
        int b = Integer.parseInt(str3); // 将字符串 str3 转换为整型，并赋值给 b
        System.out.println("b = " + b);
    }
}
```

#### 内存寻址与变量

> 不深究, 每一个数据都会在内存中有对应的位置

#### 从键盘输入

> 从键盘输入需要通过 Scanner类 结合 System.in 来获取用户输入
* Scanner类 全名 java.util.Scanner 能够从多种来源读取数据:控制台,文件,互联网
* System.in 从键盘读取数据,但一次只能读取一个字符

```java
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
```


### 级别三 条件语句：if else

#### 条件语句：if else

> 程序需要能够适应不同的情境：在一种情况下做这一些事，在另一种情况下做另一些事
> 在 Java 中，这通过条件语句实现——关键字 if 和 else，它们允许根据条件的真值执行不同的语句块

> 语句块 多条语句合并成一个块,需要用大括号包裹起来


1. 运算符 if else

```java
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
```

2. 条件语句 - 运算符

数字比较运算符
* ==
* !=
* >
* <
* >=
* <=

字符串比较
* equals() 方法 `System.out.println("aaa".equals("aa"));`


#### 布尔类型boolean与逻辑运算符

> 条件语句的结果都是布尔类型
> 数字比较运算符的结果都是布尔类型

1. 布尔数据类型:boolean

只有两个值:
* true
* false

> 不能给 boolean 类型的变量赋予其他任何值

System.out.println(1==1); // true
System.out.println(1>2);  // false

2. 逻辑运算符

> 当有两个或更多的条件时,需要通过逻辑运算符进行组合

* && 与关系
* || 或关系
* !  非关系

System.out.println( (1 > 0) && (1 < 0)); // false
System.out.println( (1 > 0) || (1 < 0)); // true
System.out.println( ! (1 == 1) ); // false


#### 运算符优先级与条件中的括号

> 当有多个条件的时候通过使用括号说明优先级 -- 简单粗暴有效
> 运算符的方向: 从左到右
> 括号 -- 处理复杂条件的最佳伙伴

运算符优先级:
1. ()
2. !
3. ==, !=
4. >, <, >=, <=
5. &&
6. ||

> && 相当与逻辑乘法, || 相当于逻辑加法
> && || ! 不要用成 and or not (这里是java,不是python)


#### Java 中的三元运算符：简洁条件与注意事项

Condition ? Expression1 : Expression2;

```java
int score = 65;
String result = score > 80 ? "优秀" : "一般";
System.out.println(result);
```

> 是否使用三元运算符的经验: 逻辑能写在一行就用,否则就不用
> 上面是开玩笑的, 大脑精力有限, 怎么简单就怎么来


### 级别四 while循环:入门与使用细节

> 存在很多任务或操作是需要重复多次的, 就要使用到循环

#### while循环:入门与使用细节

while循环的原理: 判断条件语句,条件成立,执行代码块.然后下一轮循环,直到条件不成立,循环结束

```java
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
```

#### for循环:入门与使用细节

> for循环的原理:提前设定好循环规则,根据循环规则进行循环

```java
for (初始化; 条件; 更新)
{
    // 循环体
}
```

```java
public class TestFor {
    public static void main(String[] args) {
        // 打印一百次你好 
        for (int i = 1; i <= 100; i++) {
            String message = "第" + i + "次: 你好";
            System.out.println(message);
        }
    }
}
```

```java
public class Solution {
    public static void main(String[] args) {
        // 从 (1, 5) 开始，每轮同时移动两个对象
        for (int x = 1, y = 5; x <= 5; x++, y--) {
            System.out.println(x + " " + y);
        }
    }
}
```

#### do-while循环: 入门与使用细节

> do-while循环: 先执行一次循环体, 再开始普通的while循环

语法格式:
```java
do
{
    // 循环体: 这段代码至少会执行一次
}
while (condition);
```

```java
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
```


#### 循环控制:break与continue语句

当你需要中途退出循环 或 跳过本次循环后续指令的的时候使用 `break continue` 关键字

* break 停止循环
* continue 跳过本轮次循环


### 级别五
