import { useState } from 'react';

function Square({value, onSquareClick}) { //creating the square, giving it a value, and giving it an onclick function
  return (
    <button className="square" onClick={onSquareClick}> {/* every square is a button */}
      {value}
    </button>
  );
}

export default function Board() {
  const [xIsNext, setXIsNext] = useState(true); // Each time a player moves, xIsNext(current player move)
  const [squares, setSquares] = useState(Array(9).fill(null)); // ['O', null, 'X', 'X', 'X', 'O', 'O', null, null]
  function handleClick(i) { //handle when click occurs
    if (calculateWinner(squares) || squares[i]) { //checks each square 
      return;
    }
    const nextSquares = squares.slice(); //to make copys of the board 
    if (xIsNext) { //while your turn is true
      nextSquares[i] = 'X'; //the next position will use 'x'
    } else { //while your turn is false
      nextSquares[i] = 'O'; //the next position will use 'o'
    }
    setSquares(nextSquares); //sets next turn to x or o
    setXIsNext(!xIsNext); //if false its 'O' turn, if true its 'X' turn
  }

  const winner = calculateWinner(squares); //
  let status; //empty variable
  if (winner) { //If there is a winner
    status = 'Winner: ' + winner; //Winner: X      or Winner: O 
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O'); //Next player will show whos turn it is based on the xIsNext variable defined earlier.
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        {/*squares[indices]: [0    ,1    ,2   ,3   ,4   ,5   ,6    ,7   ,8]*/}
                {/*squares: ['O', null, 'X', 'X', 'X', 'O', 'O', null, null]*/}
                  {/* squares[box] onclick will run handleclick() above */}
        <Square value={squares[0]} onSquareClick={() => handleClick(0)} />
        <Square value={squares[1]} onSquareClick={() => handleClick(1)} />
        <Square value={squares[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onSquareClick={() => handleClick(3)} />
        <Square value={squares[4]} onSquareClick={() => handleClick(4)} />
        <Square value={squares[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onSquareClick={() => handleClick(6)} />
        <Square value={squares[7]} onSquareClick={() => handleClick(7)} />
        <Square value={squares[8]} onSquareClick={() => handleClick(8)} />
      </div>
    </>
  );
}
//The layout is
//[0][1][2]
//[3][4][5]
//[6][7][8]
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2], //across top row
    [3, 4, 5], //across mid row
    [6, 7, 8], //across bottom row
    [0, 3, 6], //down left column
    [1, 4, 7], //down middle column
    [2, 5, 8], //down right column
    [0, 4, 8], //diagonal, top left to bottom right
    [2, 4, 6], //diagonal, top right, to bottom left
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i]; 
    //   checks a is not null, and checks if a and b are same symbol, checks if a and c are same symbol
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null; // no winner so dont do anything
}