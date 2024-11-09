import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useState } from "react";

const ACharacterPage = () =>{
    const { id } = useParams(); //returns an object where the id has a key of the character id
    const [character,setCharacter] = useState(null)

    const getCharacterDetails = async() =>{
        let {data} = await axios.get(`https://rickandmortyapi.com/api/character/${id}/`)
        setCharacter(data)
    }

    useEffect(()=>{
        getCharacterDetails()
    },[id])

    return (
        <>
            {character ? (
        <>
        <h2>Character Name {character.name}</h2>
        <img src="character.image"/>
        <ul>
            <li>status: {character.status}</li>
            <li>gender: {character.gender}</li>
            <li>species: {character.species}</li>
            <li>created: {character.created}</li>
        </ul>
        </>
        ) :null}
        </>
    )
}

export default ACharacterPage