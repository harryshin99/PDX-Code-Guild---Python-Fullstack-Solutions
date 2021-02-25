
// let grade = prompt("Enter your grade")

// if (grade >= 90 && grade <= 100) {
//     alert("You got an A")
// }
// else if (grade >= 80 && grade < 90) {
//     alert("You got an B")
// }
// else if (grade >= 70 && grade < 80) {
//     alert("You got a C")
// }
// else if (grade >= 60 && grade < 70) {
//     alert("You got a D")
// }
// else {
//     ("You got a F")
// }

let header = document.querySelector("#header")
let input = document.querySelector("#userInput")
let button = document.querySelector("#changeHeader")
let colorPicker = document.querySelector("#colorPicker")

// console.log(header)

// alert(header.innerText)

// header.style = "color: red;"

header.style.color = "red"
header.style.fontSize = "4em"
// console.log(header.innerText)

button.addEventListener('click', function() {
    // alert(input.value)
    header.innerText = input.value
    header.style.color = "red"
})

header.addEventListener('click', function() {
    header.style.color = colorPicker.value
    // console.log(colorPicker.value)
})



function sayHello(message) {
    alert(message)
}

let sayHello2 = function(message) {
    alert(message)
}

let sayHello3 = (message) => {
    alert(message)
}

let sayHello4 = message => alert(message)

let colors = ["blue", "green", "red", "yellow"]