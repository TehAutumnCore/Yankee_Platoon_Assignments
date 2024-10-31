import axios from "axios";

function MainUI() {
    const getPokemon = async() => {
    const random = Math.floor(Math.random() * 1025 + 1)
        try {
            let {data} = await axios.get(`https://pokeapi.co/api/v2/pokemon/${random}`)
            console.log(data)   
            // console.log(data.sprites.front_default);
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