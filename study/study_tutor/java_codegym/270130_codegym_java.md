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

