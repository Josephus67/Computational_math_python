//AI generated sample quizzes

class Person{
    constructor(
        name,
        age,
        gender,
        hobbies,
    ){
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.hobbies = hobbies;
    }
    sayHello(){
        return `Hello, my name is ${this.name}`;
    }
}

const john= new Person(
    "John",
    25,
    "male",
    ["reading", "painting", "hiking"],
);
const jane = new Person(
    "Jane",
    30,
    "female",
    ["cooking", "gardening", "painting"],
);
console.log(jane.hobbies);
console.log(john.sayHello());
console.log(jane.sayHello());