# this
- 解析器在调用函数每次会传递一个隐含参数，这个隐含参数就是this,this指向一个对象，这个对象称为函数执行的**上下文对象**
- 根据函数的调用方式不同，this会指向不同的对象
   - 1、以函数形式调用，this为window
   -  2、以方法形式调用，谁调用方法，this是谁
   -  3、以构造函数调用，this是新创建的对象
   -  4、使用call、apply时this为指定的对象
  
```js
var name= "全局name：小红";
function fun1() {
    console.log(this.name);//使用this，不同方式调用，来得到不同结果
    // console.log(name);//只能向上找全局变量
}
var obj1 = {
    name:"obj1小明",
    sayName:fun1
};
var obj2 = {
    name:"obj2小麦",
    sayName:fun1
};

console.log(obj1);
console.log(obj2);

fun1();//1、函数形式调用，this为window
obj1.sayName();//2、以方法形式调用，谁调用方法，this是谁
obj2.sayName();//2、以方法形式调用，谁调用方法，this是谁
console.log(obj1.sayName == fun1);//true
```

```js
function fun3(a,b) {
    console.log("a=" +a," b=" +b);
    console.log(this);//1、以函数形式调用，this为window

}
fun3(123,234);

var name= "全局name：小红";
function fun1() {
    console.log(this.name);//使用this，不同方式调用，来得到不同结果
    // console.log(name);//只能向上找全局变量
}
var obj1 = {
    name:"obj1小明",
    sayName:fun1
};
var obj2 = {
    name:"obj2小麦",
    sayName:fun1
};
console.log(obj1);
console.log(obj2);

fun1();//1、函数形式调用，this为window
obj1.sayName();//2、以方法形式调用，谁调用方法，this是谁
obj2.sayName();//2、以方法形式调用，谁调用方法，this是谁
console.log(obj1.sayName == fun1);//true
```