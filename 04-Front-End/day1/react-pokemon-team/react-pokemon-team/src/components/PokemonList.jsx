import React from 'react'
import Pokemon from './Pokemon'

//take list of pokemon as a prop
// render a bunch of <pokemon/> from that data
export default function PokemonList({pokemons, desiredPokemonType}) {
    console.log('<PokemonList/>')
    // console.log('<PokemonList/>')
    // console.log('props',props)
    // console.log('props.pokemon',props.pokemons)
    // console.log('props.foo',props.foo)
    
    // console.log('props.pokemon',props.pokemon)

    //same as props.pokemons
    //const pokemons = props.pokemons
    //const foo = props.foo
    //const {pokemons, foo} = props

    console.log('destructured pokemon from obj', pokemons)

    //Make an array that only has the pokemon we want and none of the ones we dont

    // let desiredPokemons=[]
    // for(let i=0; i< pokemons.length; i++){
    //     if (pokemons[i].type === desiredPokemonType) {
    //         desiredPokemons.push(pokemons[i])
    //     }
    // }

    const desiredPokemons = pokemons.filter(p => p.type === desiredPokemonType)
    console.log('desiredPokemons', desiredPokemons)

    return (
        <div> PokemonList
            <h3>PokemonList</h3>
            {/* {pokemons.map((poke,i) => ( //does the loop above)
                <Pokemon key={i} name={poke.name} type={poke.type}/>
            ))}
            {desiredPokemons.map((poke,i)=>(
                <Pokemon key={i} name={poke.name} type={poke.type} />
            ))} */}

            {pokemons
            .filter((p)=> p.type === desiredPokemonType)
            .map((p,i)=>(
                <Pokemon key={i} name={p.name} type={p.type} />
            ))}
        </div>
    );
}