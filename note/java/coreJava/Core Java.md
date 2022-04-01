# Core Java

## 第三章 java的基本程序设计结构

- 数组的声明只是申明了一个数组，并没有实例化（初始化）。

## 第五章 继承

- final 类中的所有方法都是final方法，abstract 类中的方法可以都不是abstract方法

- 抽象类不能被实例化，但是可以定义一个抽象类的对象变量，但是只能引用非抽象子类的对象。

- private<default<protected<public

- 除了基本类型的值不是对象，其他都是对象

- 泛型数组列表

  1. `arrayList.ensurecapacity(100)`分配100个对象的内部数组

  2. `new ArrayList<>(100)`和`new Employee[100]`不同（前者在最初都不会有任何元素）

  3. `arrayList.trimToSize()`在确认数组列表不会再改变时用这个方法,削减数组列表的容量到当前容量

  4. 一个巧妙的办法 

     ```java
     ArrayList<X> list = new ArrayList<>();
     while(...){
       x = ...;
       list.add(x);
     }
     X[] a = new X[list.size()];
     list.toArray(a);
     ```


- `...`省略号表明热议数量的，如：`Object...` 与`Object[]`相同
- 枚举类
  - 尽量不要构造新的对象  



## 收集的函数

- `a instanceof B`运算符是用来在运行时指出对象`a`是否是特定类`B`的一个实例 ,返回`boolean`值。注：`null instanceof B`除外
- a.getClass() 获得所属对象的类
- a.equals(b) 数组的话就用`Arrays.equals(arrayA,arrayB)`方法调用
- `hashcode` 是由对象导出的一个整数值
  - `String` hashCode 是由内容导出，而`StringBuilder`则是对象导出的
  - `a.hashcode()` 返回对象的散列码
  - `hash(obj1,obj2,...,objn)`获得提供对象的组合散列码
  - `hashCode(obj)`如果`obj`为`null`则返回0，否则返回`obj.hashCode()`


- `printStackTrace()`将Throwable对象和栈的轨迹输出到标准错误流


---

## 总结

今天学了挺多东西的，除了反射，其它都完全看懂了，反射是个好东西，记得以前我们的小波老师说过，怎么只传一个对象参数就可以知道所有的类型，答案就是使用反射来解决。反射果然很强大。以后要好好学习呢！

