console.log("HELLO YANKEE PLATOON!")

let guessHistory = []
let goal = Math.floor(Math.random() * 100);

// Your function(s) should go here that will interact with the webpage or DOM
function guessingGame(event) {
    event.preventDefault()
    console.log('in function', event)
    let userGuess = document.getElementById('num').value
    console.log('The guess is: ', userGuess)
    guessHistory.push(userGuess)
    console.log('This is the guess history: ', guessHistory)
    console.log('The guess is ', goal)
    let displayGuess = document.getElementById("guessHistory").innerText
    document.getElementById('guessHistory').innerText = displayGuess
    console.log('This is the display guess:', displayGuess)
}

console.log(guessingGame(10))
//Math.floor(Math.random() * (number + 100));