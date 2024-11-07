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

//Tutorial challenge

const bookTitle = "welcome home";
const bookAuthor = "Jane Austen";
const bookISBN = "9780198518555";
const bookPubYear = "1871-06-18";
function Book(title,author,isbn,pubYear){
    this.title = title;
    this.author = author;
    this.isbn = isbn;
    this.pubYear = pubYear;
    this.getSummary = function(){
        return `${this.title} was written by ${this.author} in ${this.pubYear}`;
    }
}

const result = new Book(bookTitle,bookAuthor,bookISBN,bookPubYear);
console.log(result.getSummary());
console.log(result.title);
console.log(result.author);
console.log(result.isbn);
console.log(result.pubYear);
