console.log("Hello World");

let income: number = 300;
let ic : string = "The miz";
let age: number = 30;
let club: string = "Real Madrid";
const isFamous: boolean = true;
let height: number = 1.80;

console.log(`My name is John Doe, I'm ${age} years old, I play for ${club}. I'm ${isFamous ? "very famous" : "not famous"}. My height is ${height} meters.`);

if (age < 50) {
    age +=10;
    console.log(`I'm ${age} years old now.`);
}

let user: [number, string] = [1,"Joe"];

enum size {small=1, medium, large}
let mySize = size.medium
console.log(`Size ${mySize} is my shoe size`)

function calculateTax(income : number){
    return 'bingo is my name'+ income
}

function calculateTax1(income : number): number {
    return income
}

function calculateTax2(income: number, taxYear:number=2022):number{
    if (taxYear < 2025){
        return income*0.3
    }
    return income*1.3
} 
console.log(calculateTax2(1000,2022));

type EmployeeType = {readonly id: number, name: string}

let employee: EmployeeType = {id:1, name: 'Employee'}
//employee.id=200;
employee.name='Josephus'

function kgToLbs (weight : number | string): number {
    if (typeof weight === 'number'){
        return weight*0.3
    }
    else{
        return parseInt(weight)*0.3
    }
}

console.log(kgToLbs(10))
console.log(kgToLbs('10'))

type Qty = 50 | 100 | 200
let pack1 : Qty = 50
let pack2 : Qty = 100
let pack3 : Qty = 200


function greet(name : string | null | undefined){
    if (name){
        console.log(name.toUpperCase()) ;
    }
    else{
        console.log('Hello!')
    }
}

greet(null)