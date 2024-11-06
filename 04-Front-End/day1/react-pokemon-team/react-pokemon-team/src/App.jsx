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
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Hello Pokemon World!</h1>
      <PokemonList/>
    </>
  )
}

export default App
