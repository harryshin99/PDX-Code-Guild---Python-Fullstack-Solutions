
const title = document.querySelector('#title')
const userInput = document.querySelector('#cc-number')

console.log(title)

title.style = "color: blue;"
title.style = "font-size: 4em;" //overrides previous styling

title.style.color = "blue" // does not override previous styling

title.innerText = "Hello World" // overrides inner text

// userInput.addEventListener('input', function() {
//     console.log(userInput.value)
// })

userInput.addEventListener('input', function() {
    title.innerText = userInput.value
})