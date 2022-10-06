// defined a variable with an integer
let x = 5
// performed an operation on that variable
x = x + 5

function localScopeExample() {
    let x = 'local scope value of x' // locally declared, only exists within function
    console.log(x)
}

console.log(x) // prints our globally declared var
localScopeExample() // prints our locally declared var

function overwritingGlobalScope() {
    x = 'local value overriding global val'
}

console.log('global var value ' + x) // print global var
overwritingGlobalScope() // overwrite global var
console.log('global var overwrritten ', x) // prints overwritten global var
// defined a function with an argument named x
function printMyVar(x) {
    console.log(x)
}

// called a function and passed it argument
//printMyVar(x)
//printMyVar('hello world')

// JS Primitive types

// Undefined
let z; // var z has no value
//console.log(z)

/** Variable declaration Examples */

// `let` allows you to reassign the value of a primitive
let letVar = 5
letVar = 13

// `const` does not let us reassign primitives
const constVar = 'hello'
// constVar = 12 // would throw an error

const constArray = ['zeroth', 'first', 'second', 'third']

console.log('const array ', constArray)
let val = constArray.pop()
console.log('val we popped out of the array ', val)
console.log('modified const array ', constArray)

// Accessing the zeroth element in an array
const zerothElement = constArray[0]
console.log(zerothElement)
// Accessing the first element in an array
const firstElement = constArray[1]
console.log(firstElement)
// Accessing the second element in an array
const secondElement = constArray[2]
console.log(secondElement)

// Add something to an array by 'pushing' it on to the array
constArray.push('third')
console.log('array with stuff pushed onto it ', constArray)

/** JS Objects */
let typeOfSomething = typeof 'hello'
console.log(typeOfSomething )

console.log(typeof 'world')
console.log('type of array ', typeof constArray)
console.log('type of function ', typeof localScopeExample)

let user = {
    // object properties
    x: 13,
    name: 'Tom', // key `name`, value 'Tom'
    age: 34, // key `age`, value '34'
}

console.log('user object ', user)
console.log('user name ', user.name)
console.log('user name ', user['name'])

// Add a property to an existing object
user.favoriteFood = 'chicken'
user['favoriteColor'] = 'blue'

console.log('updated user object ', user)

const keyName = 'cityOfBirth'

function catchPhrase(lastWord) {
    const phrase = 'How cool, ' + lastWord
    console.log(phrase)
    return phrase;
}

// Executing the function
catchPhrase()

// Execute the function and assign its output to a variable
const phrase = catchPhrase('bro!')

// assign function as a variable
// JS has first-class functions - functions can be passed as vars or arguments
let myCatchPhrase = catchPhrase;

// Call the function we assigned to the variable
myCatchPhrase('Bro!!!')

const userAccount = {
    info: {
        firstName: 'Adam',
        lastName: 'Cahan',
        [keyName]: 'Chicago',
        // don't do it this way
        'favoriteColor': 'blue',
    },
    favoriteNumbers: [1,2,3,4,5],
    myPhrase: catchPhrase,
}

userAccount.info.email = `${userAccount.info.firstName}${userAccount.info.lastName}@codeplatoon.org`

console.log(userAccount)

userAccount.myPhrase('dude!')

function getCompanyEmail(user) {
    const firstName = user.info.firstName;
    const lastName = user.info.lastName;

    // One way of doing string concatenation
    const email = firstName + lastName + '@codeplatoon.org'
    // Or Use tagged template literal for string concatenation
    const emailAnotherWay = `${firstName}${lastName}@codeplatoon.org`

    return emailAnotherWay;
}

const adamEmail = getCompanyEmail(userAccount)
console.log(adamEmail)