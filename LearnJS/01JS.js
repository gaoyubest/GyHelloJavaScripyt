alert("我是引用外部JS文件");

var condition = true;
if(condition){
    //语句体
}else if (false){
    //
}else {
    //
}

while (condition){
    //
}

do {
    //
} while (condition);

var result = 0;
for (var i=0; i<=100; i++){
    result +=i;
}
console.log(result);


function isShui(num) {
    if (num >=100 && num <= 999){
        var a = Math.trunc(num/100);
        var b = Math.trunc(num/10)%10;
        var c = Math.trunc(num%10);
        if (Math.pow(a,3)+Math.pow(b,3)+Math.pow(c,3) === num){
            return 1;
        }else{
            return 0;
        }
    }else{
        return 2;
    }
}