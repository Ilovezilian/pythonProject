# jQuery调用a标签的click方法
```html
<a id="myA" href="#abc" />
```
使用jQuery调用a的click方法进行调用失败
```js
$("#myA").click();
$("#myA").trigger("click");
```

但是用下面的可以
```js 
document.getElementById("myA").click();
```

网上搜了一下解决方案
```js 
$("#myA")[0].click();
```

## 思考
`$("#myA")`
获取的的是id为myA的a标签的jQuery元素，而jQuery选中的元素中并没有click触发方法法，所以调用失败。
而`$("#myA")[0]`则是 获取a这标签的标签元素，而这个元素是有click方法，所以调用可以成功；

