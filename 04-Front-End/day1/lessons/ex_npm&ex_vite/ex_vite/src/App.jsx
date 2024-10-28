import axios from 'axios'
import './App.css'


function App() {
  // capture user input for desired pokemon name/id
  // make request for front sprite from pokeapi
  // render image for user
  // reset input field to blank
  
  const createImg = (url) => {
    let img = document.createElement("img") //<img src='#'/>
    img.src = url
    img.className = 'pokemon-img'
    document.getElementById('img-container').appendChild(img)
  }

  const getPokemonImg = async(poke) => {
    try{
      // let resp = await fetch(`https://pokeapi.co/api/v2/pokemon/${poke}`)
      let resp = await axios.get(`https://pokeapi.co/api/v2/pokemon/${poke}`)
      // let data = await resp.json()
      let data = resp.data
      return data.sprites.front_default
    }
    catch(err){
      console.err(err)
      return null
    }
  }

  const handleSubmit = async(evt) => {
    evt.preventDefault()
    let input = document.getElementById('user-input')
    let usrInput = input.value
    let imgUrl = await getPokemonImg(usrInput)
    createImg(imgUrl)
    input.value = ''
  }

  return (
    <>
      <form onSubmit={(evt)=>handleSubmit(evt)}>
        <input id='user-input' type="text" placeholder='pokemon name'/>
        <input type='submit'/>
      </form>
      <div id='img-container' className='a-class'>
      </div>
    </>
  )
}

export default App