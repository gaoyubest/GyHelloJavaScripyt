# 函数：
函数也是对象，可以封装一些功能（代码）
**创建函数：**
```js
//第一种：构造函数
var fun1 = new Function("console.log('Hello1')");
fun1();

//第二种：
function fun2() {
    console.log('Hello2');
}
fun2();

//第三种：函数表达式
var fun3 = function () {
    console.log('Hello3');
};
fun3();

```

**函数—形参、实参**
**形参**：相当于在函数内部声明了对应的变量
```js
//sum（）调用函数，相当于传递函数返回值
//sum函数对象，相当于使用函数对象
function sum(a,b) {
    // console.log(a+b);
    return a+b;
}
console.log("result= " + sum(2,3));


//实参：用对象传递实参
function Xinxi(o) {
    console.log("我的名字叫：" + o.name +"，今年我" +
                o.age +"岁了，" + "性别是：" + o.gender);
}
var obj = {
    name:"翟小坏",
    age:23,
    gender:"男"
};
Xinxi(obj);

//实参：函数作为实参传递
function fun4(a) {
    a(obj);
}
fun4(Xinxi);

//实参：传递匿名函数
fun4(function() {
    console.log("Hello匿名函数")
});
```
**立即执行函数：**
定义完立即被调用，只会执行一次
```js
(function(a,b) {
    console.log("a=" +a);
    console.log("b=" +b);
})(1,6);
```
**返回值：**
- 可以是任意类型，也可为对象,也可以为函数
- return直接跳出
```js
function fun5() {
    // return {name:"翟小坏"};
    function fun6() {
        console.log("fun5内部声明的函数fun6");
    }
    return fun6;
}
var result1 = fun5();
console.log("result1= " + result1.name);
console.log(result1);
```

# 方法
- 函数也可以称为对象的属性。
- 函数作为对象的属性保存，这个函数为**对象的方法**。只是名称上的区别。
```js
//创建对象
var obj1 = new Object();

//对象属性赋值
obj1.name = "小红";
obj1.age = 18;

//对象的属性值可以为函数
//方法一：
obj1.sayName = function () {
    console.log(obj1.name);
};


function fun1() {
    console.log(obj1.name);
}
// console.log(obj1.sayName);

//调方法
obj1.sayName();
//调函数
fun1();

//方法二：
var obj2 = {
    name:"小明",
    age:23,
    sayName:function () {
        console.log(obj2.name);
    }
};
obj2.sayName();
```
# arguments
- 调用函数时，浏览器每次都会传递两个隐含参数
  - 1、函数的上下文对象this
  - 2、封装实参对象arguments，arguments是一个类数组对象,可以通过索引来操作数据，也可以获取长度。在调用函数时，我们所传递的实数会在arguments中保存。即使不定义形参，也可以传递实参。callee对应的函数对象为正在执行的对象
```js
function fun() {
    console.log(Array.isArray(arguments));
    console.log(arguments.length);//获取实参长度
    console.log(arguments[1]);
    console.log(arguments.callee);
}
fun("hello",true);
```