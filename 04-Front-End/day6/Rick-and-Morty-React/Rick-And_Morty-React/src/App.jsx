import { useState } from 'react'
import './App.css'
import HomePage from './pages/HomePage'
import { Outlet } from 'react-router-dom'

function App() {

  return (
    <>
      <h1>Hello World!</h1>
      <Outlet/>
    </>
  )
}

export default App
