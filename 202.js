const { Console } = require("console");

console.log("whats up brothers")
//String concatenation

//Using the “+” operator
let firstName= "Joesphus ";
let surName="Bawah";
console.log(firstName+surName);
//Using the template literals (${``})
//the back tick is used here (`) ie where the symbol (~) is, instead of the single quotes(')
let fullName = `This is the life ${surName}, ${firstName} decided to live`;
let FullName= `my name is ${firstName}${surName} and i am a boy`
console.log(fullName);
console.log(FullName)

let radius=14;
let pi=22/7
let area= `The area of the circle is ${(pi).toFixed(2)*(radius)**2}`;
console.log(area)

//ternary operator (short hand for the if else condition)
let age=5
let status=age >=18 ? 'adult' : "minor";
console.log(status);

//switch case

let day='a';

switch(day){
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("tues");
        break;
    case 3:
        console.log("wed")
        break;
    default:
        console.log("invalid input")
}
//console.log(day)

let monthss=8
switch(monthss){
    case 1:
        console.log("winter");
        break;
    case 2:
        console.log("Winter");
    case 3:
        console.log("winter");
        break;
    case 4:
        console.log("spring");
        break;
    case 5:
        console.log("spring");
        break;
    case 6:
        console.log("spring");
        break;
    case 7:
        console.log("summer");
        break;
    case 8:
        console.log("summer");
    case 9:
        console.log("Summer");
        break;
    case 10:
        console.log("autumn");
        break;
    case 11:
        console.log("autumn");
    case 12:
        console.log("autumn");
        break;
    default:
        console.log("invalid month of the year")
}

let month = 5;

switch (true) {
  case month >= 1 && month <= 3:
    console.log("Winter");
    break;
  case month >= 4 && month <= 6:
    console.log("Spring");
    break;
  case month >= 7 && month <= 9:
    console.log("Summer");
    break;
  case month >= 10 && month <= 12:
    console.log("Autumn");
    break;
  default:
    console.log("Invalid month");
}

let months = 5;

switch (months) {
  case 1:
  case 2:
  case 3:
    console.log("Winter");
    break;
  case 4:
  case 5:
  case 6:
    console.log("Spring");
    break;
  case 7:
  case 8:
  case 9:
    console.log("Summer");
    break;
  case 10:
  case 11:
  case 12:
    console.log("Autumn");
    break;
  default:
    console.log("Invalid month");
}

//for loops
for (i=0; i<=10; i++){
    console.log(i)
}

let person={ fname:"joe", lname: "bawah", age:25}
let text=""
for (let x in person){
   console.log(text+=person[x])
}

//functions
function greet(name){
    console.log(`Hello ${name}!`)
}
greet("joe")

function sum(a,b){
    return a+b
}
console.log(sum(2,3))

function avg(a,b){
  return((a+b)/2)
}
console.log(avg(2,3))

//function to say hello to the user
//let nmae1="Josephus";
//let name2="Joe"
function hello(nmae1,name2){
  welcome=`hello ${nmae1}, can we call you ${name2}?`
  return welcome
}
console.log(hello("Josephus","Joe"))

//function to find the mean of a set of numbers
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,19];

hello =function mean(X) {
  let sum = 0;
  for (let i = 0; i < X.length; i++) {
    sum += X[i];
  }
  return (sum / X.length).toFixed(2);
}

//console.log(mean(X)); 

console.log(hello(X))

function helllo() {
  console.log("Hello!!");
}
helllo();
//console.log(helllo());

//arrow functions
function emm(name3){
  console.log(`Hello, ${name3}!!, mtf`)
}
emm("Joe");

const emmm=(name4)=>{
  console.log(`Hello, ${name4}!!, mtf`) 
}
emmm("joe");

function add1(a, b) {
  return a + b;
}
const add2=(a,b)=>{
  return a+b;
}

console.log(add2(2,3));

function square(X){
  return X*X;
}
console.log(square(4))

const Asquare=(Y)=>{
  return Y**2;
}
console.log(Asquare(4));

const AAsquare=(Z)=>Z*Z;
 console.log(AAsquare(4))

 //Anonymous functions
 