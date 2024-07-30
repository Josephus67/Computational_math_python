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
