console.log("Hello world")

const getPokemonImg = (imgSrc) => {
    let imgContainer = document.querySelector("#container")
    let img = document.createElement('img') 
    img.src = imgSrc
    img.style.width = '25vmin'
    img.style.height = "25vmin"
    img.style.border = 'solid 1px black'
    imgContainer.appendChild(img)
}

//create a function
const getpokemonFrontDefault = () => {
    let num = Math.floor(Math.random() * 100)
    fetch("https://pokeapi.co/api/v2/pokemon/${num}") //fetch gets a response "generates a promise"
        .then((response)=>response.json()) //turn response into json data and generates promise
            .then((data)=>{ //
                let front_default = data.sprites.front_default
                // console.log(front_default)
                getPokemonImg(front_default)
    })
    .catch((err)=>{
        alert("something went wrong")
    })
}



const getRickSanchez = async() => {
    try{    
        const response await fetch("https://rickandmortyapi.com/api/character")
        const data = await response.json()
        getPokemonImg(data.img)

    }
    catch(err) {
    }
}

//generate a random number between 1 and 1000
//fetch pokemon data corresponding to rand int
//iterate through response to grab front_default sprite
//return front_default sprite