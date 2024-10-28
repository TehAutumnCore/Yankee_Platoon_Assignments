import axios from "axios"

const sayHello = () => {
  return "Hello"
}

const getPokemonFetch = () => {
  fetch("https://pokeapi.co/api/v2/pokemon/ditto")
    .then((resp)=>{
      return resp.json()
    })
    .then((data)=>{
      console.log(data.sprites.front_default)
    })
}

const getPokemon = () => {
  axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
    .then((resp)=> {
      console.log(resp.data.sprites.front_default)
    })
    .catch((err)=>{
      console.log(err)
    })
}
getPokemon()
getPokemonFetch()

// module.exports = {sayHello}