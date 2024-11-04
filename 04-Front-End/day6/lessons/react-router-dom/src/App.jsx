import { useState } from 'react'
import './App.css'
import {Outlet} from react-router-dom
import {Link} from react-router-dom
import NavBar from './components/NavBar'

function App() {
  const [user,setUser] = useState(null)

  UseEffect(()=>{
    console.log(user)
  },[user]
)
  return (
    <>
      <NavBar/>
      <button onclick={()=>setUser("I'm a user")}>Register</button>
      <Outlet />
      {/* <HomePage/>
      <About/>
      <ContactPage/> */}
      <h1>footer</h1>
    </>
  )
}

export default App
