let allChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

let length = prompt("How long do you want your password to be? Please enter a whole number: ")

let password = ""

let counter = 0
while (counter < length) {
    randChar = allChar[Math.floor(Math.random()*allChar.length)]
    password += randChar
    counter++
}

alert(`Your password is ${password}`)