import { useState } from 'react'
import './App.css'
import PokemonList from './components/PokemonList'

/***
 * install axios
 * add a button
 * make <PokemonList/>
 * make <Pokemon/>
 * make api call to get all pokemon
 * render a list of a bunch of pokemon
 * get unique pokemon types ?? HOW??
 * add a dropdown of pokemon type options
 * when drop selected, make api call to get 5 pokemon of type
 * render those pokemon in the list
 */
function App() {
  const fakePokemon=[
    {name:'Charizard', type: 'fire'},
    {name:'Pikachu', type: 'electric'},
    {name:'Ditto', type: 'normal'}
  ]

  const desiredPokemonTypes = 'normal' //create prop
  //Get fakePokemons into PokemonList by passing as a prop
  return (
    <>
    <div>
        <h1>Pokemon App</h1>
        <PokemonList pokemons={fakePokemon} desiredPokemonTypes = {desiredPokemonTypes}/> 
        {/* const props={
            pokemons: fakePokemons,
            foo: 'hello'
            }                 */}
      </div>
    </>
  )
}

export default App
