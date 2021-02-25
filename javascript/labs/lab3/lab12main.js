
alert("Welcome to Black Jack advisor. Your available cards are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K")

let firstCard = prompt("Enter is your first card: ").toUpperCase()
let secondCard = prompt("Enter is your second card: ").toUpperCase()
let thirdCard = prompt("Enter is your third card: ").toUpperCase()

let cardValues = {
    A: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    J: 10,
    Q: 10,
    K: 10
}

// let firstCardValue

for (value in cardValues) {
    if (firstCard == value) {
        firstCardValue = cardValues[value]
    }
}

for (value in cardValues) {
    if (secondCard == value) {
        secondCardValue = cardValues[value]
    }
}

for (value in cardValues) {
    if (thirdCard == value) {
        thirdCardValue = cardValues[value]
    }
}

let total = firstCardValue + secondCardValue + thirdCardValue

if (total < 17) {
    alert(`${total}: Hit`)
}
else if (total >= 17 && total < 21) {
    alert(`${total}: Stay`)
}
else if (total == 21) {
    alert(`${total}: Blackjack!`)
}
else {
    alert(`${total}: Already Busted`)
}