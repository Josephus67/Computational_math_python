"use strict";
console.log("Hello World");
let income = 300;
let ic = "The miz";
let age = 30;
let club = "Real Madrid";
const isFamous = true;
let height = 1.80;
console.log(`My name is John Doe, I'm ${age} years old, I play for ${club}. I'm ${isFamous ? "very famous" : "not famous"}. My height is ${height} meters.`);
if (age < 50) {
    age += 10;
    console.log(`I'm ${age} years old now.`);
}
let user = [1, "Joe"];
var size;
(function (size) {
    size[size["small"] = 1] = "small";
    size[size["medium"] = 2] = "medium";
    size[size["large"] = 3] = "large";
})(size || (size = {}));
let mySize = size.medium;
console.log(`Size ${mySize} is my shoe size`);
function calculateTax(income) {
    return 'bingo is my name' + income;
}
function calculateTax1(income) {
    return income;
}
function calculateTax2(income, taxYear = 2022) {
    if (taxYear < 2025) {
        return income * 0.3;
    }
    return income * 1.3;
}
console.log(calculateTax2(1000, 2022));
let employee = { id: 1, name: 'Employee' };
employee.name = 'Josephus';
function kgToLbs(weight) {
    if (typeof weight === 'number') {
        return weight * 0.3;
    }
    else {
        return parseInt(weight) * 0.3;
    }
}
console.log(kgToLbs(10));
console.log(kgToLbs('10'));
//# sourceMappingURL=index.js.map