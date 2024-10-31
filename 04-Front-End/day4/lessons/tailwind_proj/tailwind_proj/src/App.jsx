import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className="text-3xl font-bold underline">Hello world!</h1>
      <button className='px-5 py-1 border-2'>click me</button>
      <div id='container' className='absolute top-0 left-0 w-full h-full flex justify-center items-center gap-x-2'>
        <div className='box'></div>
        <div className='box'></div>
        <div className='box'></div>
      </div>
    </>
  )
}

export default App
