import './App.css'
import { Outlet } from 'react-router-dom'
import NavBar from './components/NavBar'
import { useEffect } from 'react'

function App() {
  const [favorites, setFavorites] = useState([])

  const isFavorite = (character) =>{
    return favorites.includes(character)
  }

  const addFavorite = (character) => {
    setFavorites([...favorites, character]) //using ... to grab all the values within the favorites array + the character being added
  } 

  const rmFavorite = (character) =>{
    setFavorites(favorites.filter((char)=> char.id != character.id))
  }

  useEffect(()=>{
    console.log(favorites)
  },[favorites])

  return (
    <>
      <h1>Rick and Morty</h1>
      <NavBar/>
      <Outlet context={{isFavorite,addFavorite,rmFavorite}}/>
    </>
  )
}

export default App
