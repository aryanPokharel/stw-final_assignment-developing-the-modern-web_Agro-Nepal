//this js section is just for trial purpose
/*
var name='Aryan';
console.log('name before section is',name)

{
    let name = 'Mr. Aryan'
    console.log('name inside section is',name)
}
console.log('name after section is',name)
*/


/*
let Name = 'Aryan'
let age = 20;
Object
 person = {
    fname: 'Aryan',
    lname: 'Pokharel',
    address: 'Jhapa'
}

console.log(person.fname, person.lname, person.address)
*/

//Arrays and for loop
/*
var array1 = ['Ram', 'Shyam', 'Hari', 'Gopal'];
var i = 0;
for (i in array1){
    console.log(array1[i],)
}
*/

/*functions in JS

function sayHi(name) {
    console.log("Hi!", name);
    return console.log("Function executed!")
}

var num = 9;
if (num==90){
    sayHi(num)
}
*/

/* setting default values for parameters in functions 
function add(num1 = 0, num2 = 1){
    sum = num1 + num2;
    console.log("The sum is "+ sum);
}

add();
*/

/* Arrow Functions 
const add = (num1 = 0, num2 = 1) => console.log(num1+num2);
add();
//These functions come handy when the function has only one line of code to execute like in the example above. The function returns the output of code after the arrow sign!
*/


/*objects and embeded objects (objects within objects) 


const person = {
    fName: 'Aryan',
    lName: 'Pokharel',
    age: 20,
    address: {
        Province: 'Province-1',
        District: 'Jhapa',
        localLevel: 'Mechinagar'
    }
}
console.log("first name :", person.fName);
console.log("District : ", person.address.District);

*/

/* To Do list example 
const todos = 
[
    {
        id: 1,
        task: 'Workout',
        isCompleted: true
    },
    {
        id: 2,
        task: 'Read a book',
        isCompleted: true
    },
    {
        id: 1,
        task: 'Watch TV',
        isCompleted: false
    }
];
console.log(todos[1].task);
*/


/* for loops 

for (let i = 0; i < 5; i++){
    console.log("Step number : "+ (i+1));
}
*/
 
/* while loops 
let i = 0;
while(i<8){
    console.log("Step number : " + (i+1));
    i++;
}
*/


/* forEach 
const todos = 
[
    {
        id: 1,
        task: 'Workout',
        isCompleted: true
    },
    {
        id: 2,
        task: 'Read a book',
        isCompleted: true
    },
    {
        id: 1,
        task: 'Watch TV',
        isCompleted: false
    }
];
todos.forEach(function(todo){
    console.log(todo.task);
})
*/

/* map 
const todos = 
[
    {
        id: 1,
        task: 'Workout',
        isCompleted: true
    },
    {
        id: 2,
        task: 'Read a book',
        isCompleted: true
    },
    {
        id: 1,
        task: 'Watch TV',
        isCompleted: false
    }
];
const todoText = todos.map(function(todo){
    return (todo.task);
})
console.log(todoText);
*/

/* filter 

const todos = 
[
    {
        id: 1,
        task: 'Workout',
        isCompleted: true
    },
    {
        id: 2,
        task: 'Read a book',
        isCompleted: true
    },
    {
        id: 1,
        task: 'Watch TV',
        isCompleted: false
    }
];
const todoCompleted = todos.filter(function(todo){
    return (todo.isCompleted == true);
})
console.log(todoCompleted);
*/


/*   */

/* a == b implies that the values of a and b are equal
    a === b implies that the values as well as the datatypes of a and b are equal
*/

/* Ternery Operator example 

const a = 11;

const type = (a % 2 === 0) ? 'even' : 'odd';
// in the above line, ? refers to 'then' and ':' refers to else
console.log(type);
*/


/* Switch/case statements 

const color = 'blue';

switch(color){
    case 'red' :
        console.log('The color is red!')
        break;
    case 'blue':
        console.log('The color is blue!')
        break;

    default:
        console.log('It is colourless!')
        break;
}
*/

/* Constructor function 
function Person(fname, lname, dob, address){
    this.FirstName = fname;
    this.LastName = lname;
    this.dob = new Date(dob);
    this.address = address;
}

//Instantiating the function

const person1 = new Person('Aryan', 'Pokharel', '10-24-2000', 'Dhat');
const person2 = new Person('Kashyap', 'Koirala', '2-01-2001', 'Bazar');

console.log(person1, person2)
*/

/* Prototype functions: We can add some methods/function to classes separately at different scopes
so that only required instances can run those functions, as per the need.
*/
/*
function Person(fname, lname, dob, address){
    this.FirstName = fname;
    this.LastName = lname;
    this.dob = new Date(dob);
    this.address = address;
}
Person.prototype.getFullName = function() {
    return `${this.fname} ${this.lname}`;
}

person1 = Person('Ram', 'Thapa', '2-2-2002', 'gulmi')
person2 = Person('Shyam', 'Yadav', '2-2-2009', 'Dolpa')
console.log(person2.getFullName());
*/

/* General old way of classes and methods */
/*
class Person{
    constructor(fname, lname, dob, address){
        this.firstName = fname;
        this.lastName = lname;
        this.dob = new Date(dob);
        this.address = address;
    }
    getFullName(){
        return `${this.firstName} ${this.lastName}`;
    }
    getAddress(){
        return this.address; 
    }
}

const aryan =new Person('Aryan', 'Pokharel', '10-24-2000', 'Jhapa');
console.log(aryan.getFullName())
*/















