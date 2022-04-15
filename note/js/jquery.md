# jquery-- Using jQuery Core

## $ vs $()
通过jquery对象调用jQuery方法，这样的方法叫做`$.fn`命名空间,或者`jQuery prototype`，这样的方法很多。
``` js
$( "h1" ).remove();
```
还有小部分的的方法是jQuery命名空间的一部分，作为jQuery的核心方法。
> `$.fn`命名空间方法被jQuery选择器调用，自动接收并且返回选择器作为`this`
> `$`命名空间通常是实用型方法不通过选择器调用，参数和返回值不限

## $( document ).ready()
* `$( document ).ready()`只会在页面DOM(document)加载完成之后执行一次
* `$( window ).on( "load", function() { ... })`只会在整个页面(window)加载完成之后执行一次（不仅仅是DOM）--

### 集中使用方式

``` js
// A $( document ).ready() block.
$ (document ).ready(function() {
    console.log( "ready!" );
});

// Shorthand for $( document ).ready()
// `$()` 是 `$( document ).ready()` 的缩写.
$(function() {
    console.log( "ready!" );
}):

// Passing a named function instead of an anonymous function.
function readyFn( jQuery) {
    // Code to run when the document is ready.
}
$( document ).ready( readyFn );
// or :
$( window ).on( "load", readyFn );
```
## Avoiding Conflicts with Other Libraries
为了jQuery.js不与prototype.js,MooTools,YUI等命名空间缩写的冲突，做了如下避免冲突的方式
### 使jQuery进入不冲突模式

* 用`$j`作为jQuery的缩写别名解决别名冲突
```js w<-- Putting jQuery into no-conflict mode..-->
<script src="ptorotype.js"></script>
<script src="jquery.js"></srcipt>
<script>
var $j = jQuery.noConflict();
// $j is now an alias to the jQuery function; create the new alias is optional.
$j( document ).ready(function() {
    $j( "div" ).hide();
});

// The $ variable now has the prototype meaning, which is a shortcut for 
// document.getElementById(). mainDiv below is a DOM element, not a jQuery object.
window.onload = function() {
    var mainDiv = $( "main" );
}
</script>
```
* 用`$`作为jQuery的缩写别名解决别名冲突
```js 
<!-- - Another way to put jQuery into no-conflict mod. -->
<script src="prototype.js"></script>
<script src="jquery.js"></script>
<script>
jQuery.noConflict();
// 使用方式是 jQuery( document ).ready() 使用 `$`作为参数即可
jQuery( document ).ready(function( $ ) {
     // you can use the locally-scoped $ in here as an alias to jQuery.
    $( "div" ).hid();
});
// The $ variable in the global scope has the prototype.js meaning.
window.onload = function() {
    var mainDiv = $( "main" );
}
</script>
```
### 提前加载jQuery库
提前加载的话，因为`$`已经被重新定义了，所以就不需要时用jQuery.noConflict()处理冲突的情况。
```js 
<!-- Loading jQuery before other libraries. -->
<script src="jquery.js"></script>
<script src="prototype.js"></script>
<script>
 
// Use full jQuery function name to reference jQuery.
jQuery( document ).ready(function() {
    jQuery( "div" ).hide();
});
 
// Use the $ variable as defined in prototype.js
window.onload = function() {
    var mainDiv = $( "main" );
};
 
</script>
```

## Attributes
```js 
//`.attr()` as a setter
$( "a" ).attr( "href", "allMyHerefsAreTheSameNow.html" );

$( "a" ).attr({
    title: "all titles are the same too!",
    href: "somethingNew.html"
});

//`.attr()` as a getter
$( "a" ).attr( "href" ); // returns the href for the first a element in the document
```
## Selecting Elements
大部分情况下，jQuery是选择元素并在选择的元素上进行操作
```js 
### Selecting Elements by ID
$( "#myId" ); ### Note IDs must be unique per page.

### Selecting Elements by Class Name
$( ".myClass" );

### Selecting Elements by Attribute
$( "input[name='first_name']" );

### Selecting Elements by Compound CSS Selector
$( "#contens ul.people li" );

### Selecting Elements with a Comma-separated List of Selectors
$( "div.myClass, ul.people" );

### Pseudo-Selectors
$( "a.external:first" );
$( "tr:odd" );

// Select all input-like elements in a form (more on this below).
$( "#myForm :input" );
$( "div:visible" );

// All except the fitst three divs.
$( "div:gt(2)" );

// All currently animated divs.
$( "div:animated" );

```
### Choosing Selectors
测试选择器是否有元素
```js 
// wrong $() 表达式的返回永远是有对象的，所以不能这么校验是否有元素
if ( $( "div.foo" )) {
    ... 
}
// yes $().length 来测试$()是否有元素
// Testing whether a selection contains elements.
if ( $( "div.foo" ).length ) {
    ...
}

// Refining selections.
$( "div.foo" ).has( "p" ); // div.foo elements that contain <p> tags
$( "h1" ).not( ".bar" ); // h1 elements that don't have a class of bar    
$( "ul li" ).filter( ".current" ); // unordered list items with class of current
$( "ul li" ).first(); // just first unordered list item
$( "ul li" ).eq( 5 );  // the sixth

//Selecting Form Elements

:checked 只用于选择框 checkboxes, radio buttons, selects
$( "form :checked" );

:disabled :enable 用于输入框 <input>
$( "form :disabled" );
$( "form :enabled" );

:input 用于 <input>, <textarea>, <select>, <button>
$( "form :input" );

:selected 用于<option> 元素
$( "form :selected" );

// other
:password
:reset
:radio
:text
:submit
:checkbox
:button
:image
:file
```

## Working with Selections

jQuery 对象方法可以用于取值和赋值，不带参数为取值，带参数为赋值。
另外jQuery对象方法的返回值是jQuery对象，这样可以继续调用jQuery方法，这貌似是叫做调用链。

## Manipulating Elements
### Getting and Setting Information About Elements
* .html() - Get or set the HTML contents.
* .text() - Get or set the text contents; HTML will be stripped.
* .attr() - Get or set the value of the provided attribute.
* .width() - Get or set the width in pixels of the first element in the selection as an integer.
* .height() - Get or set height in pixels of the first element in the selection as an integer.
* .position() - Get an object with position information ofr the first element in the selection, relative to its first positioned another ancestor. This is a getter only.
* .val() - Get or set the value of from elements.
### Moving, Copying, and Removing Elements
**Moving**

* .insertAfter() .after()
* .insertBefore() .before()
* .appendTo() .append()
* .prependTo() .prepend()

**Cloning**

* .clone  // If you need to copy related data and events, be sure to pass true as an argument to .clone().

**Removing**

* .remove() // doesn't return removed elements, not have associated data and events attached 
* .detach() // return removed elements, remain data and events attached
* .empty() dispose of the element's inner HTML

### Creating New Elements

* $()
```js
// Creating new elements from an HTML string.
$( "<p>This is a new paragraph</p>" );
$( "<li class=\"new\">new list item</li>" );

// Creating a new element with an attribute object.
$( "<a/>", {
    html: "This is a <strong>new</strong> link",
    "class": "new",
    href: "foo.html"
});
```
上面创建的元素还不能及时的展示在页面上，还需要通过下面操作:
```js 
// Getting a new element on to the page.
var myNewElement = $( "<p>New eselement</p>" );
myNewElement.appendTo( "#content" );
myNewElement.insertAter( "ul:last" ); // This will remove the p from #content!
$( "ul" ).last().after( myNewElement.clone() ); // Clone the p so now we have two.

// Creating and adding an element to the page at the same time.
$( "ul" ).append( "<li>list item</li>" );

```
### Manipulating Attributes

* .attr()
````js 
// manipulating a single attribute.
$( "#myDiv a:first" ).atrr( "href", "newDestination.html" );

// Manipulating multiple attributes.
$( "#myDiv a:first" ).attr({
    href: "newDestination.hmtl",
    rel: "nofollow"
});

// Using a function to determine an attribute's new value.
$( "#myDiv a:first" ).attr({
    rel: "nofollow",
    href: function( idx, href ) {
    return "/new/" + href;
    }
});
$( “#myDiv a:first" ).attr( "href", function( idx, href ) {
    return "/new/" +href;
});
````
## The jQuery Object
相对Web的DOM操作，jQuery对象有两个优点:compatibility（兼容）, convenience（方便）
### Getting Elements into the jQuery Object
jQuery选择器方法返回jQuery对象包装的选择元素
```js 
// Selecting all <h1> tags.
var headings = $( "h1" );

// viewing the number of <h1> tags on the page. 
var headings = $( "h1" );
alert( headings.length );

// Selecting only the first <h1> element on the page in a jQuery object)
var headings = $( "h1" );
var firstHeading = headings.eq( 0 );

// Selecting only the first <h1> element on the page.
var firstHeadingElem = $( "h1" ).get( 0 );

// Selecting only the first <h1> element on the page (alternate approach).
var firstHeadingElem = $( "h1" )[ 0 ];
```
无论包装的对象是不是相同的，jQuery包装的对象都是不相等的（不能用== 或者 ===进行比较）
```js  
// Comparing DOM elements (with more readable variable names).
 
var $logo1 = $( "#logo" );
var logo1 = $logo1.get( 0 );
 
var $logo2 = $( "#logo" );
var logo2 = $logo2.get( 0 );
 
alert( $logo1 === $logo2 ); // alerts "false" 
alert( logo1 === logo2 ); // alerts "true"
```

## Traversing
### Parents
* .parent() .parents() .parentsUtil() .closest()
```html
<div class="grandparent">
    <div class="parent">
        <div class="child">
            <span class="subchild"></span>
        </div>
    </div>
    <div class="surrogateParent1"></div>
    <div class="surrogateParent2"></div>
</div>

```
```js 
// Selecting an element's direct parent:
// returns [ div.child ]
$( "span.subchild" ).parent();

// Selecting all the parents of an element that match give selector:
// returns [ div.parent ]
$( "span.subchild" ).parents( "div.parent" );
// returns [ div.child, div.parent, div.grandparent ]
$( "span.subchild" ).parents();

// Selecting all the parents of an element up to, but *not include* the selector:
// returns [ div.child, div.parent ]
$( "span.subchild" ).parentsUtil( "div.grandparent" );

// Selecting the closest parent, note that only one parent will be selected
// and that the initial element itself is included in the search:
// returns [ div.child ]
$( "span.subchild" ).closest( "div" );
// returns [ div.child ] as the selector is also included in the search:
$( "div.child" ).closest( "div" );
```
### Children
```js 
// Selecting an element's direct children:
// returns [ div.parent, div.surrogateParent1, div.surrogateParent2 ]
$( "div.grandparent" ).children( "div" );

// Finding all elements within a selection that match the selector:
// returns [ div.child, div.parent, div.surrogateParent1, div.surrogateParent2 ]
$( "div.grandparent" ).find( "div" );
```
### Siblings 
```js 
// Selecting a next sibling of the selectors:
// returns [ div.surrogateParent1 ]
$( "div.parent" ).next();

// Selecting a pre sibling of the selectors:
// returns [] as No sibling exists before div.parent
$( "div.parent" ).prev();

// Selecting all the next siblings of the selector:
// returns [ div.surrogateParent1, div.surrogateParent2 ]
$( "div.parent" ).nextAll();
// returns [ div.surrogateParent1 ]
$( "div.parnet" ).nextAll().first();
// returns [ div.surrogateParent2 ]
$( "div.parent" ).nextAll().last();

// Selecting all the previous siblings of the selector:
// returns [ div.surrogateParent1, div.parent ]
$( "div.surrogateParent2" ).prevAll();
// returns [ div.surrogateParent1 ]
$( "div.surrogateParent2" ).prevAll().first();
// returns [ div.parent ]
$( "div.surrogateParent2" ).prevAll().last();

// Selecting an element's siblings in both directions that matches the given selector:
// returns [ div.surrogateParent1, div.surrogateParent2 ]
$( "div.parent" ).siblings();
// returns [ div.parent, div.surrogateParent2 ]
$( "div.surrogateParent1" ).siblings();
```

## CSS, Styling, & Dimensions
```js 
// Getting CSS properties.
$( "h1" ).css( "fontSize" ); // Returns a string such as "19px".
$( "h1" ).css( "font-size" ); // Also works.

// Setting CSS properties. 很少使用
$( "h1" ).css( "fontSize", "100px" ); // Setting an individual property.

// Setting multiple properties.
$( "h1" ).css({
    fontSize: "100px",
    color: "red"
});

// Working with classes 常用
var h1 = $( "1" );
h1.adClass( "big" );
h1.removeClass( "big" );
h1.toggleClass( "big" );
if ( h1.hasClass( "big" ) ) {
    ...
}

// Basic dimensions methods.
// Sets the width of all <h1> elements.
$( "h1" ).width( "50px" );
// Gets the width of the fist <h1> element.
$( "h1" ).width();
//Sets the height of all <h1> elements.
$( "h1" ).height( "50px" );
// Gets the height of the first <h1> element.
$( "h1" ).height();

// Returns an object containing position information ofr the first <h1> relative to its "offset (positioned) parent".
$( "h1" ).position();
```
## Data Methods
```js 
// Storing and retrieving data related to an element.
$( "#myDiv" ).data( "keyName", { foo: "bar" } );
$( "#myDiv" ).data( "keyName" ); // Returns { foo: "bar" }

// Storing a relationship between elements using .data()
$( "#myList li" ).each(function() {
    var li = $( this );
    var div = li.find( "div.content" );
    li.data( "contentDiv", div );
});

// Later, we don't have to find the div again;
// we can just read it from the list item's data
var firstLi = $( "#myList li:first" );
firstLi.data( "contentDiv" ).html( "new content" );
```

## Utility Methods
* $.clearQueue()
* $.dequeue()
* $.boxModel
* $.browser
* $.contains()
* $.data()
* $.dequeue()
* $.each()
* $.extend()
  *  jQuery.extend([deep ,] target [, object1 ] [, objectN ] ) 
  * *Merge the contents of two or more objects together into the first object.*   target will change,and return target.
* $.fn.extend()
* $.globalEval()
* $.grep()
* $.inArray()
* $.isArray()
* $.isEmptyObject()
* $.isFunction()
* $.isNumeric()
* $.isPlainObject()
* $.isWindow()
* $.isXMLDoc()
* $.makeArray()
* $.map()
* $.merge()
* $.noop()
* $.now()
* $.parseHTML()
* $.parseJSON()
* $.parseXML()
* $.proxy()
* $.queue()
* $.removeData()
* $.support
* $.trim()
* $.type()
* $.unique()
* $.uniqueSort()
* $ queue()

## Iterating over jQuery and non-jQuery Objects
$.each()
```js 
var sum = 0;
var arr = [1,2,3,4,5];
for (var i = 0; l = arr.length; i < l; i ++ ) {
    sum += arr[ i ];
}
cosole.log( sum ); // 15 

$.each( arr, function( index, value ) {
    sum += value;
});

console.log( sum ); // 15

var sum = 0;
var obj = {
    foo: 1,
    bar: 2
}
for (var item in obj) {
    su += obj[ item ];
}
console.log( sum ); // 3

$.each( obj, function( key, value ) {
    sum += value;
});
console.log( sum ); // 3

```

.each
```html
<ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <li><a href="#">Link 3</a></li>
</ul>
```
```js 
$( "li" ).each( function( index, element ) {
    console.log( $( this ).text() );
// Logs the following: Link 1; Link2; Link 3;

$( "li" ).each( function( index, listItem ) {
 
    this === listItem; // true
 
    // For example only. You probably shouldn't call $.ajax() in a loop.
    $.ajax({
        success: function( data ) {
            // The context has changed.
            // The "this" keyword no longer refers to listItem.
            this !== listItem; // true
        }
    });
 
});

```
$.map()
```js 
var newArr =[];
$( "li" ).each( function() {
    newArr.push( this.id );
});
// return JavaScript array
$( "li" ).map( function( index, element) {
    return this.id;
}).get();

```
.map()
```js 
<li id="a"></li>
<li id="b"></li>
<li id="c"></li>

<script>
var arr = [{
    id: "a",
    tagName: "li"
},{
    id:"b",
    tagName:"li"
},{
    id:"c",
    tagName:"li"
}];

// Returns [ "a","b","c"]
$( "li" ).map( function( index, element ) {
    return element.id;
}).get();

// also returns [ "a", "b", "c" ]
// Note that the value comes first with $.map
$.map( arr, function( value, index ) {
    return value.id;
});
</script>
```

## Using jQuery’s .index() Function
.index() gives the zero-based index of jQuery object within its parent.
```html
<ul>
    <div></div>
    <li id="foo1">foo</li>
    <li id="bar1">bar</li>
    <li id="bazl">baz</li>
    <div></div>
</ul>
```
```js 
var foo = $( "#foo1" );
console.log( "Index: " + foo.index() ); // 1

var listItem = $( "li" );
// This implicitly calls .first()
console.log( "Index:" + listItem.index() ); // 1
console.log( "Index:" + listItem.first().index() );// 1

var div = $( "div" );
// This implicitly calls .first()
console.log( "Index:" + div.index() ); // 0
console.log( "Index:" + div.first().index() ); // 0
```
.index(arg)
When .index() is called with a string argument, there are tow things to consider.
first, jQuery will implicitly call .first on the original jQuery object. find the first element。
second, jQuery is querying the entire DOM using the passed in string selector and checking the index within that newly queried jQuery object.

```html
<ul>
    <div class="test"></div>
    <li id="fool">foo</li>
    <li id="barl" class="test">bar</li>
    <li id="bazl">baz</li>
    <div class="test"></div>
</ul>
<div id="last"></div>
```
```js 
var foo = $( "li" );
// This implicitly calls .first()
console.log( "Index:" + foo.index( "li" ) ); // 0
var baz = $( "#bazl" );
console.log( "Index:" + baz.index( "li" )); // 2
var listItem = $( "#barl" );
console.log( "Index:" + listItem.index( ".test" ) ); // 1
var div = $( "#last" );
console.log( "Index:" + div.index( "div" ) ); // 2

console.log( "Index:" +foo.index( baz ) ); // 2
var tests = $( ".text" );
var bar = $( "#barl" );
// Implicitly calls .first() on the argument.
console.log( "Index:" + tests.index( bar ) ); // 1
console.log( "Index:" + tests.index( bar.first() ) ); // 1
```

.index() with a jQuery Object Argument search the first element of jQuery object
.index() with a DOM element argument just search the element

## Frequently Asked Questions
### How do I select an item using class or ID?

```js 
$( "#ID" )
$( ".ClassName" )
```

### How do I select elements when I already have a DOM element?

```js
var myDocElement document.getElementById( "foo" );
$( myDocElement ).find( "a" );

```
### How do I test whether an element has a particular class?

```js
$( this ).hasClass( “className" )
```

### How do I test whether an element exists?

```js
$( "#ID" ).length
```
### How do I determine the state of a toggled element?
### How do I select an element by an ID that has characters used in CSS notation?

```js
// Does not work
$( "#ID :id" )
// work
$( "#ID\\:id" )
// Does not work
$( "#ID .id" )
// work
$( "#ID\\.id" )
```

### How do I disable/enable a form element?

```js
$( "#ID" ).prop( "disabled", true );
$( "#ID" ).prop( "disabled", false );

```

### How do I check/uncheck a checkbox input or radio button?
```js
$( "#ID" ).prop( "checked", true );
$( "#ID" ).prop( "checked", false );
```
### How do I get the text value of a selected option?

```html
<select id="myselect">
    <option value="1">Mr</option>
    <option value="2">Mrs</option>
    <option value="3">Ms</option>
    <option value="4">Dr</option>
    <option value="5">Prof</option>
</select>
```
```js
$( "#myselect option:selected" ).text(); // => "Mr"
$( "#mySelect" ).val(); // => 1
```

### How do I replace text from the 3rd element of a list of 10 items?

```js
$( this ).find( "li a" ).eq( 2 ).text( "hello world" );
```
### How do I pull a native DOM element from a jQuery object?

```js
$( "#ID" )[0]
$( "#ID" )get(0)
```














