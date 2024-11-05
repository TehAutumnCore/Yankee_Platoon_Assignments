import axios from "axios";

function getRandomPokemon() {
    const [selectedTypes, setSelectedTypes] = ([])
    const [pokemonData, setPokemonData] = ([])
    const getPokemon = async() => {
    const random = Math.floor(Math.random() * 1025 + 1)
        try {
            let {data} = await axios.get(`https://pokeapi.co/api/v2/pokemon/${random}`)
            const types = data.types
            const selectedTypes = types[1] ? [types[0].type.name,types[1].type.name] : [types[0].type.name];
            // console.log(selectedTypes)
            setPokemonData(data)
            console.log(data.name)
            // console.log(data.types[0])   
            // console.log(data.types[1])
            // console.log(data.sprites.front_default);
            // console.log(data.types);
    } catch(error) {
        console.error("An error occurred", error);
        }
        return data
    }

    const getPokemonType = async(type) => {
        let {data} = await axios.get(`https://pokeapi.co/api/v2/type/${type}`)
        const type_list = data.pokemon.slice(0,5) //list of 5 pokemon dicts
        const pokemonData = await Promise.all(type_list.map(async(pokemon)=>{
            const pokemon_url =  await axios.get(pokemon.url)
                return pokemon_url.data
        }))
        return pokemonData
    }

    const setTeam = async() => {
        const randomPokemon = await getRandomPokemon()
        randomPokemon.types.map(()=>{

        })
    }

    return(
        <>
            <h1>Click the button for a pokemon!</h1>
            <button onClick={getPokemon}>Button</button>
            <div id="container">
                <div className="displaypokemon"></div>
            </div>
        </>
        );
    }

export default MainUI