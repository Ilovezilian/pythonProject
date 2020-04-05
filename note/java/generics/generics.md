# 泛型
## 概念
抽象的数据类型，运行的时候才使用的具体的类型

> this long-awaited enhancement to the type system allows a type or method to operate on objects of various types while providing compile-time type safety.

类型对象变量保障在虚拟机编译时的类型安全，并被一个类型或者方法操作，这是一个对于类型系统的增强。

### 相关术语
* ArrayList<E>中的E称为类型参数变量, 也叫形式类型参数（formal type parameters）
    * 常用大写的单个字母表示泛型变量：
    * E for element 
    * T for type
    * K for keys 
    * V for values

* ArrayList<Integer>中的Integer称为实际类型参数（actual type argument）
* 整个称为ArrayList<E>泛型类型
* 整个ArrayList<Integer>称为参数化的类型（parameterized type）

## 核心
敲代码的时候总是会遇到强制类型转换，每次遇到总是想用一种方式确保它不会出现，毕竟那个代码太丑以至于受不，而且很容易因为书写错误导致转换报错。

强制一个自己定义的类中不需要重复代码而且可以指定数据的类型，从此去掉强制转换导致的转换错误和代码优雅，是泛型的核心。

1. 泛型的理解
形式类型参数会被实际的类型替换掉，换个角度理解：形式类型参数就是类型变量。

2. 泛型初始化
对于所有的声明过的泛型类型实际上在虚拟机只进行过一次初始化为单例的类文件，就像普通的类和接口一样。

3. 泛型变量

### 泛型关系
泛型变量对应的对象是继承关系，但是不代表确定泛型变量的泛型是继承关系。
如：Foo 继承 Bar 但是：G<Foo> 不继承 G<Bar>
> 泛型变量只是变量，就是变量用实际的类型替换了，单也只是泛型的一个参数，实际上的的继承关系还是按照G的继承关系来的。混淆就不好了吧(^\_^)

## 语法规则
### 泛型接口
只能用在抽象方法上
### 泛型类
只能用在成员变量上，不能用在静态成员变量上，毕竟泛型类只初始化一次，但是泛型成员变量只有在对象运行的时候才知道对应的对象是啥，就没法在静态成员变量上使用类层次使用泛型类参数。
只能使用引用类型
1. 声明
```java
public class myClass<T>{ 
    public void myMethod(T t, S s) {}
    public T myMethod(T t) {}
    public T myMethod(List<T> list, T t, S s) {}
}
```
### 方法
1. 参数
    1. 上限 extends
    2. 下限 super
    3. 并且 &
```java
public class myClass{ 
    public <T> T myMethod(T t) {}
    public T myMethod(List<T> list, T t, S s) {}
    public <T extends S, S> List<T> myMethod(List<T> list, T t, S s) {}
}
```
## 泛型类型声明&通配符&通配类型

### 概念

> Collection<?> (pronounced "collection of unknown")
统配符`?` 表示：未知的类型，可以用来匹配任意类型，称为统配类型

通配类型只能用于读取数据，不能用于修改数据。
因为要修改的任意类型都会被认为是任意类型的子类，并不是任意类型所以不能修改这个类型的数据。
读取数据的时候可以用Object类型进行声明，因为统配类型说到底也是一个对象，所以可以用Object进行声明。

### 通配符界限

> Wildcards are designed to support flexible subtyping, 
> which is what we're trying to express where allow a variety of actual argument types to be used at different invocation sites.

通配符设计通过在不同场景使用多种实际参数类型来支持灵活拓展子类型的一种表达方式。

```java
 public class myClass<T> {
    public T myMethod(T t) {
        return t;
    }

    /** 通配符上限
     * @param t*/
    public void myMethod1(List<? super T> t) {
        // read
        // add compile error
        System.out.println("t = " + t);
    }
    /** 通配符下限 */
    public T myMethod(List<? extends T> t) {
        // read
        // add compile error
        return t.get(0);
    }
    public T myMethod(List<T> list, T t) {
        return t;
    }
}
```

### 泛型方法
泛型方法用来表示一个或者多个方法参数类型或者返回值的依赖关系，如果没有这层依赖关系，不建议使用。

```java
public static class myClass<T>{
    public <E> List<E> myMethod(List<E> list, E t) {
        return list;
    }
    public static <T> void copy(List<T> dest, List<? extends T> src) {} // 和下面等价
    public static <T, S extends T> void copy(List<T> dest, List<S> src) {}
}
public class myClass<T>{ 
    public <E> List<E> myMethod(List<E> list, E t) {}
    public <E> List<E> myMethod(List<E> list, E t) {}
  
    public static <T, S extends T> void copy(List<T> dest, List<S> src) {}
}
```


## 兼容老版本
兼容包括：
    泛型调用原型代码；
    原型调用泛型代码；

消除转换法
消除掉所有泛型，转化为原始类型

## 拓展 参考
> In general, if you have an API that only uses a type parameter T as an argument, its uses should take advantage of lower bounded wildcards (? super T). Conversely, if the API only returns T, you'll give your clients more flexibility by using upper bounded wildcards (? extends T).

```java
public class Collections<E> {
    public static <T extends Comparable<T>> T max(Collection<T> coll){}
    public static <T> T writeAll(Collection<T> coll, Sink<? super T> snk) {}
}
```

## 要点（The Fine Print）
### 所有变量参数类型的泛型对象都共享一个泛型类的类实例
```java 
    List <String> l1 = new ArrayList<String>();
    List<Integer> l2 = new ArrayList<Integer>();
    System.out.println(l1.getClass() == l2.getClass());
    //  true
```
### 在泛型类上使用instanceOf是没有意义的

```java 
    Collection cs = new ArrayList<String>();
    // Illegal.   Illegal generic type for instanceof
    if (cs instanceof Collection<String>) {}
```
### Casts强制转换会导致泛型对象的程序不可信
```java 
// Unchecked warning. 
<T> T badCast(T t, Object o) {
    return (T) o;
}
```
### 数组
> if your entire application has been compiled without unchecked warnings using javac -source 1.5, it is type safe.

1. 可以创建通配符的泛型对象数组，但是不可以创建有对象参数的泛型对象数组。
> 为了避免未检查警告导致的运行错误
```java 
// Not really allowed.
List<String>[] lsa = new List<String>[10];
Object o = lsa;
Object[] oa = (Object[]) o;
List<Integer> li = new ArrayList<Integer>();
li.add(new Integer(3));
// Unsound, but passes run time store check
oa[1] = li;

// Run-time error: ClassCastException.
String s = lsa[1].get(0);
```
```java 
// OK, array of unbounded wildcard type.
List<?>[] lsa = new List<?>[10];
Object o = lsa;
Object[] oa = (Object[]) o;
List<Integer> li = new ArrayList<Integer>();
li.add(new Integer(3));
// Correct.
oa[1] = li;
// Run time error, but cast is explicit.
String s = (String) lsa[1].get(0);
```
2. 不能创建泛型数组。
> 因为不知道类型变量在运行时不存在所以没办法判断是什么类型的数组，所以不能创建数组。
```java
<T> T[] makeArray(T t) {
    return new T[100]; // Error.
}
```
## Class类在JDK 1.5也是泛型类































