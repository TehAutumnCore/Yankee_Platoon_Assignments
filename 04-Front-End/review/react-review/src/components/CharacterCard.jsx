import axios from "axios";
import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import App from "../App";

const CharactersPage = () => {
  const {isFavorite, addFavorite, rmFavorite}
  const [useNavigate] = 
  const [characters, setCharacters] = useState([]); // array of objects
  const [nextPage, setNextPage] = useState(null);
  const [previousPage, setPreviousPage] = useState(null);
  const [currentPage, setCurrentPage] = useState(
    `https://rickandmortyapi.com/api/character`
  );

  const getCharacters = async () => {
    let { data } = await axios.get(currentPage);
    setCharacters(data.results);
    setNextPage(data.info.next);
    setPreviousPage(data.info.prev);
  };

  useEffect(() => {
    getCharacters();
  }, [currentPage]);

//   useEffect(() => {
//     console.log('curr',currentPage);
//     console.log('prev',previousPage);
//     console.log('next', nextPage)
//   }, [currentPage, nextPage, previousPage]);

  return (
    <>
      <h2>Characters Rick and Morty</h2>
      <div
        style={{
          display: "flex",
          gap: "5vmin",
          maxWidth: "100%",
          minWidth: "100%",
          flexWrap: "wrap",
        }}
      >
        {characters.map((character) => (
          <div className="card" key={character.id}>
            <img src={character.image} />
            <p>{character.name}</p>
            <button onClick={()=>Navigate(`/character/${character.id}`)}>See More</button>
          </div>
        ))}
      </div>
      <button onClick={() => setCurrentPage(previousPage)}>Prev</button>
      <button onClick={() => setCurrentPage(nextPage)}>Next</button>
    </>
  );
};

export default CharactersPage;