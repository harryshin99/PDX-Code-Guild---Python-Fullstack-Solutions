const container = document.querySelector("#list-container")
const addButton = container.querySelector("#add-button")
const userInput = container.querySelector("#user-input")
const currentList = container.querySelector("#current-list")
const compList = container.querySelector("#list-completed")

userInput.addEventListener('keypress', function(enter) {
    if (enter.keyCode == 13) {
        addToList();
    }
})

addButton.addEventListener('click', function () {
    addToList();
})

function addToList() {
    let addItem = document.createElement('li')
    let delButton = document.createElement('button')
    let doneButton = document.createElement('button')
    addItem.innerText = userInput.value
    doneButton.innerText = "done"
    doneButton.className = "done"
    delButton.innerText = "delete item"
    delButton.className = "delete"
    addItem.appendChild(doneButton)
    currentList.prepend(addItem)
    addItem.appendChild(delButton)
    userInput.value = ""
    delButton.addEventListener('click', function() {
        addItem.remove()
        delButton.remove()
        doneButton.remove()
    })
    doneButton.addEventListener('click', function() {
        currentList.removeChild(addItem)
        compList.prepend(addItem)
    })
}



// addButton.addEventListener('click', function () {
    
//     let addItem = document.createElement('li')
//     let delButton = document.createElement('button')
//     let doneButton = document.createElement('button')
//     addItem.innerText = userInput.value
//     doneButton.innerText = "done"
//     doneButton.className = "done"
//     delButton.innerText = "delete item"
//     delButton.className = "delete"
//     addItem.appendChild(doneButton)
//     currentList.prepend(addItem)
//     addItem.appendChild(delButton)
//     userInput.value = ""
//     delButton.addEventListener('click', function() {
//         addItem.remove()
//         delButton.remove()
//         doneButton.remove()
//     })
//     doneButton.addEventListener('click', function() {
//         currentList.removeChild(addItem)
//         compList.prepend(addItem)
//     })
// })