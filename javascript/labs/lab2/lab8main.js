
let randNum = 1 + Math.floor(Math.random() * 10)

let tries = 1

while (tries < 11) {

    let userGuess = prompt("Guess a number between 1 and 10: ")

    if (randNum == userGuess) {
        alert(`You guessed the correct number! ${userGuess} was right!`)
        break
    }
    else if (tries == 10) {
        alert(`${userGuess} is incorrect. You have no more tries left. The correct number was ${randNum}. Good bye!`)
    }
    else {
        alert(`${userGuess} is incorrect. Please try again. You have ${10 - tries} tries left.`)
    }

    tries++
}
