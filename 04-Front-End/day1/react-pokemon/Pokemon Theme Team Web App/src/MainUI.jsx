import axios from "axios";

function MainUI() {
    const [selectedTypes, setSelectedTypes] = ([])
    const getPokemon = async() => {
    const random = Math.floor(Math.random() * 1025 + 1)
        try {
            let {data} = await axios.get(`https://pokeapi.co/api/v2/pokemon/${random}`)
            const types = data.types
            const selectedTypes = types[1] ? [types[0].type.name,types[1].type.name] : [types[0].type.name];
            console.log(selectedTypes)
            // console.log(data)   
            // console.log(data.types[0])   
            // console.log(data.types[1])
            // console.log(data.sprites.front_default);
            // console.log(data.types);
    } catch(error) {
        console.error("An error occurred", error);
        }
    }

    return(
        <>
            <h1>Click the button for a pokemon!</h1>
            <button onClick={getPokemon}>Button</button>
        </>
        );
    }

export default MainUI