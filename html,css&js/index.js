let head = document.getElementsByClassName("headinggg").innerHTML = "HEAD";
console.log(head);
console.log(typeof(para));
function showHide() {
    let para = document.getElementById("paraaa");
    console.log("hello");
    // let containerrr = document.getElementsByClassName("containerrr")[0];
    // let data = containerrr.getElementsByTagName("p")[0].innerHTML;
    // console.log("data = ", data);
    if (para.style.display != "none") {
        // if (data.style.display !== "None") {
            console.log("kkk");
            
            para.style.display = "none";
        }
        else{
            para.style.display = "block";
        }
    }
    // if (data != "  ") {
    //     console.log("1");

    // } else {
    //     console.log("2");
        
    // }
    // let firstHeading = document.getElementsByClassName("heading")
    // // firstHeading[1].innerText = "changed content";
// console.log(firstHeading);
// let bodyContaint = document.getElementsByClassName("container");
// console.log(bodyContaint);

// let a =  5;
// let chheckAum = a>=10 ? "tru" : "false";
// console.log(chheckAum);


// const array1 = [1,2,3,4,5,6];
// let [array2 , array3 , array4 , ...array5] = array1;
// console.log(array2, array3, array4, array5);
// console.log(array1);
// let new Array = ...array1;
// let array = [...array1];
// console.log(array);
// var array2 = [1,2,3,4,5,6,7];
// const array3 = new Array([1,6]);
// console.log(array3);


// **** objects in array ****

// const array = {
//     name : "chirag" , 
//     age : 22 , 
//     rolew : "nbnmb"
// }
// console.log(array);
// console.log(array.name);

const key = 'email';
const arrayChirag = {
    name : "chirag" , 
    age : 22 , 
    rolew : "nbnmb"
}
// console.log(arrayChirag);

// arrayChirag.key = "xhiragbkjakjdhakjsdha"
// arrayChirag['key'] = "xhiragbkjakjdhakjsdha"
arrayChirag[key] = "xhiragbkjakjdhakjsdha"
// console.log(arrayChirag);
console.log(Object.keys(arrayChirag));
console.log(typeof(Object.keys(arrayChirag)));

// const array2 = new Array();
// array2.name = "banana";
// console.log(array2);
// console.log(array);

