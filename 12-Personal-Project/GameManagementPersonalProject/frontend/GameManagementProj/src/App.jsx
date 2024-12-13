// import { useState } from 'react'
import './App.css'
import {Outlet} from "react-router-dom"
import NavBar from './components/NavBar'
import Footer from './components/Footer'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <NavBar/>
      <Outlet/>
      {/* All Pages here such as <Homepage/>, <AboutMePage/>, <LibraryPage/> etc  */}
      <Footer/>
    </>
  )
}

export default App