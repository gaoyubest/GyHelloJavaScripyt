
# Date
```js
var obj = new Date();//直接使用构造方法创建，则封住当前代码执行时间
var obj1 = new Date("12/3/2020 11:12:40");
var date = obj1.getDate();//获取当前日期对象为几号
var day = obj1.getDay();//获取当前日期对象是周几，0表示周日，0-6
var month = obj1.getMonth();//获取当前日期对象是月份，0表示一月，0-11
var year = obj1.getFullYear();//获取当前日期对象是年份

//时间戳，从格林威治标准时间的1979年1月1日，0时0分0秒到当前日期所花费的毫秒数
//一秒=1000毫秒，计算机底层保存的时间都是时间戳
var time = obj1.getTime();//获取当前日期对象是时间戳
var time1 = Date.now();//获取当前时间的时间戳

//运用时间戳测试代码的执行性能
var start = Date.now();
for(var i =0;i<100;i++){
    console.log(i);
}
var end = Date.now();
console.log("执行了"+(end - start)+"毫秒");


console.log(obj);
console.log(obj1);
console.log("date" +date);
console.log("day" +day);
console.log("month" +month);
console.log("year" +year);
console.log("time" +time/1000/60/60/24/365);//得到年
```