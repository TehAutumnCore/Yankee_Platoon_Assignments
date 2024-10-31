import { useState, useEffect } from 'react'
import Form from "react-bootstrap/Form";
import axios from 'axios'
import './App.css'

export default function App() {
  const [userInput, setUserInput] = useState("");
  const [selectedPokemon, setSelectedPokemon] = useState(null)

  const getPokemonInfo = async (e) => {
    e.preventDefault();
    const { data } = await axios.get(
      `https://pokeapi.co/api/v2/pokemon/${userInput}`
    );

    console.log(data)
    // console.log(data.abilities)
    // console.log(data.cries)
    // console.log(data.moves)
    console.log(data.sprites.front_default)
    console.log(data.sprites.front_shiny)
    setSelectedPokemon(data);
  };

  return (
    <>
      <h1 className="text-3xl font-bold underline">
        Welcome to our bootleg Pokedex
      </h1>
      <Form onSubmit={(e) => getPokemonInfo(e)}>
        <Form.Control
          className='border-solid border-4 border-indigo-500'
          placeholder='Enter a pokemon here'
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <button type="submit">Submit</button>
      </Form>
      <div className='border-solid border-4 border-fuchsia-300' id='container'>
        <div id='display_and_description'>
          <div className='display border-solid border-4 border-violet-500'>MAIN DISPLAY</div>
          <div className='description border-solid border-4 border-red-300'>Description</div>
        </div>
        <div id='button-container' className='border-solid border-4 border-red-300'>
          <div className='border-solid border-4 border-amber-500'><button>Shiny</button></div>
          <div className='border-solid border-4 border-orange-500'><button>Abilities</button></div>
          <div className='border-solid border-4 border-teal-500'><button>Moves</button></div>
          <div className='border-solid border-4 border-rose-500'><button>Cries</button></div>
        </div>
      </div>
    </>
  )
}