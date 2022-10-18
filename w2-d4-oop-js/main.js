// `this` is not attached to any object. It refers to the *context* or *scope* surrounding
// where the code that contains `this` is *executed* -- not defined.
//console.log(this)

// `this` is determined by how a function is called: In most cases, the value of this is determined by how a function is called
// The context/scope surrounding the function when its called
const alice = {
    name: 'alice',
    sayHello: function() {
        console.log(`Hello my name is ${this.alice}`)
    }
}

//alice.sayHello()

// Uncomment the line below and see what happens
//this.name = 'Global Scope Name'

const bob = {
    name: 'bob',
    sayHello: () => {
        console.log(`My name is ${this.name}`)
    }
}

// bob.sayHello()

// `this` will be the surrounding *context* of where the function is *called*
const mySayHelloFunction = function() {
    console.log(this.name)
}

const dan = {
    name: 'dan',
    sayHello: mySayHelloFunction,
}

const eve = {
    name: 'eve',
    sayHello: mySayHelloFunction,
}

// dan.sayHello()
//eve.sayHello()

// immediately invoked function expression
const foo = function(){ 
    return 'hello world'
}()

// console.log(foo)


/** Example of the module pattern -- the old way before classes */
const someVar = 13;
const myModule = function() {
    const someVar = 13 

    return {
        x: 5,
        myPrivateVar: someVar,
    }
}
//console.log('myModule')

/***
 * The `new` keyword. Many languages have a `new` keyword to create a class. Python does not have one.
 * In Python: Alice = Person('alice')
 */

const Person = function(name) {
    // const this = {}
    this.name = name

    // using `new` will return `this`, like so:
    // return this
}

const frank = new Person('frank')
//console.log(frank)

// no `this` context object returned
const frankNotWithNew = Person('frank')
// console.log(frankNotWithNew)

const bar = {}

Person.prototype.sayHello = function() {
    console.log(`Hello, my name is ${this.name}`)
}

//frank.sayHello()

/** The `class` keyword */
class Human {
    // we use constructor similarly to __init__ in python
    constructor(name) {
        this.name = name
    }

    sayHello() {
        console.log(`Hello, my name is ${this.name}`)
    }
}

const gina = new Human('Gina')
// gina.sayHello();

/** functional programming in js **/
function makePerson(personName, age) {
    return {
        name: personName,
        age: age,
        sayHello: () => console.log(`my name is ${personName}`)
    }
}

const henry = makePerson('henry')
// henry.sayHello()

const people = [
    ['ichabod', 30], 
    ['jane', 32],
]

function makePersonWrapper(personArr) {
    return makePerson(personArr[0], personArr[1])
}
const peopleObjects = people.map(
    // p => makePerson(p[0], p[1])
    makePersonWrapper,
)
console.log(peopleObjects)
