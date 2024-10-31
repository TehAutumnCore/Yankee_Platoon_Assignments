import './App.css'
import Layout from './Layout'

function App() {
  return (
    <>
      <Layout />
        <div id="measurements">
          <div className='box'>1</div>
          <div className='box'>2</div>
          <div className='box'>3</div>
          <div className='box'>4</div>
          <div className='box' id='the-box'>5</div>
          <div className='box'>6</div>
          <div className='box'>7</div>
          <div className='box'>8</div>
          <div className='box'>9</div>
          <div className='box'>10</div>
        </div></>
        {/* <div className='rm-size'>
          <p>Wow!</p>
          <div className='rem-size'>
            <p>Wow!</p>
            <div className='rem-size'>
              <p>Wow!</p>
            </div>
          </div>
        </div>
      </div>
    </> */}
  )
}

export default App
