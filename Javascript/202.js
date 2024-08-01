const { Console, error } = require("console");
const { get } = require("http");

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
 let show = function() { 
     console.log('Anonymous function')}
     show();

     let show1=()=>console.log('Arrow function')
     show1();

     let show2=()=>{console.log('Block function')}
     show2();

     //Arrays
     let numbers12 = [1, 2, 3, 4, 5];
     console.log(numbers12);


     //template literals
     let name = 'John';
     console.log(`Hello, ${name}!`);

     //default parameters
     function greet(name = 'World') {
       console.log(`Hello, ${name}!`);
     }

     greet();

     //rest parameters
     function sum(...numbers21) {
       return numbers21.reduce((total, number21) => total + number21, 0);
     }

      console.log(sum(1, 2, 3, 4, 5));
      console.log(sum(1, 2));
      console.log(sum());
      console.log(sum(...[1, 2, 3, 4, 5]));
      console.log(sum(1, 2, ...[3, 4, 5]));
      console.log(sum(1, 2, ...[3, 4], 5));
      console.log(sum(...[1, 2], 3, 4, 5));
      console.log(sum(...[1, 2, 3], 4, 5));

      const anynumber=[1,2,3,4,5,6,7,8,9,10,12,57,23];
      const array1=anynumber.find((element)=>element>10);
      console.log(array1);
      console.log(anynumber.length);
      console.log(anynumber.toString());
      console.log(anynumber.join("-"));
      console.log(anynumber.pop());
      console.log(anynumber.push(100));
      console.log(anynumber);
      console.log(anynumber.shift());
      console.log(anynumber);
      console.log(anynumber.unshift("bingo"));
      console.log(anynumber);

      //array methods
      let numbers=[1,2,3,4,5];
      console.log(numbers.includes(3));
      console.log(numbers.includes(6));
      console.log(numbers.indexOf(3));
      console.log(numbers.lastIndexOf(3));
      console.log(numbers.reverse());
      console.log(numbers);
      console.log(numbers.sort((a,b)=>a-b));
      console.log(numbers);

      //object literals
      let person1={name:"John", age:30, city:"New York"}
      console.log(person1);
      console.log(person1.name);
      console.log(person1.age);
      console.log(person1.city);
      console.log(person1.country="USA");
      console.log(person1);
      delete person1.age;
      console.log(person1);

      //array map
      let numbers2=[1,2,3,4,5];
      let doubledNumbers=numbers2.map((number2)=>number2*2);
      console.log(doubledNumbers);

      //array filter
      let numbers3=[1,2,3,4,5];
      let filteredNumbers=numbers3.filter((number3)=>number3>3);
      console.log(filteredNumbers);

      //array reduce
      let numbers4=[1,2,3,4,5];
      let sumNumbers=numbers4.reduce((total, number4)=>total+number4,0);
      console.log(sumNumbers);

      //array reduceRight
      let numbers5=[1,2,3,4,5];
      let reversedSum=numbers5.reduceRight((total, number5)=>total+number5,0);
      console.log(reversedSum);
//objects
const joejoe={
  iname:"Josephus",
  sname: "Bawah",
  age: 21,
  height: "6ft3",
  eyecolor:"blue",
}
console.log(joejoe.age);
console.log(joejoe['eyecolor']);
joejoe.nationality="Ghanaian";
console.log("nationality" && "iname" in joejoe);
for (const key in joejoe){
  console.log(`${key}:${joejoe[key]}`);
}

//constructors
function Persone(name, age, height, eyecolor){
  this.name=name;
  this.age=age;
  this.height=height;
  this.eyecolor=eyecolor;
}

const fborn= new Persone("Joe",30,"6ft3","blue")
const sborn=new Persone("Romanus",20,"6ft","green")
const tborn=new Persone("Keren",13,"5ft1","white")
const lborn= new Persone("Immaculate",10,"3ft9","pink")
console.log(fborn);
console.log(sborn);
console.log(tborn);
console.log(lborn);
console.log(fborn.name);
console.log(sborn.age);
console.log(tborn.height);
console.log(lborn.eyecolor);

function UG(studentName,ID,course,level){
  this.studentName=studentName;
  this.ID=ID;
  this.course=course;
  this.level=level;
}
const student1=new UG("Josephus",11038230,"Comp science",200);
console.log(student1);
console.log(student1.ID)
//getters
const bingo={
  _name:"John",
  _age:30,
  _height: "7ft",
  get name(){
    return this._name
  },
  get age(){
    return this._age
  },
  get height(){
    return this._height
  }
};
console.log(bingo);
console.log(bingo.name);
//error handling
try{
  console.log(bingo.height);
}catch(error){
  console.log(error);
}
console.log("hello world");
function withdraw(amount) {
  const balance=100;
  if (amount>balance){
    throw new Error("you have insufficient funds");
  }
  return balance-amount
}
try {
console.log(withdraw(50));
console.log(withdraw(150));
} catch (error){
console.error(error.message);
}

function divides(a,b){
  try{
  if (b===0){
    throw new Error("cannot divide by zero");
  }
  return a/b;
}
catch (error){
console.error(error.message);
return null;
}
}
console.log(divides(2,0));
//inheritance
/*
class Animal{
  constructor(name, age){
    this.name=name;
    this.age=age;
  }
  speak(){
    console.log(`${this.name} makes a sound`);
  }
}
  */