import './App.css'
import { Outlet } from 'react-router-dom'
import NavBAr from './components/NavBar'

function App() {

  return (
    <>
      <h1>Rick and Morty</h1>
      <NavBAr/>
      <Outlet/>
    </>
  )
}

export default App
