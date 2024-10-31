import { useEffect, useState } from "react";
import "./App.css";
import Button from "react-bootstrap/Button";
import MyModal from "./components/MyModal";
import Form from "react-bootstrap/Form";
import axios from "axios";
import PokeCard from "./components/PokeCard";

function App() {
  const [count, setCount] = useState(0);
  const [modalShow, setModalShow] = useState(false);
  const [usrInput, setUsrInput] = useState("");
  const [selectedPokemon, setSelectedPokemon] = useState(null);

  // useEffect(() => {
  //   console.log(usrInput);
  // }, [usrInput]);

  const getPokemonInfo = async (e) => {
    e.preventDefault();
    let { data } = await axios.get(
      `https://pokeapi.co/api/v2/pokemon/${usrInput}`
    );
    setSelectedPokemon(data);
  };

  return (
    <>
      <h1>Hello Yankee</h1>
      <Form onSubmit={(e) => getPokemonInfo(e)}>
        <Form.Control
          type="text"
          value={usrInput}
          onChange={(e) => setUsrInput(e.target.value)}
        />
        <Button type="submit">Look for poke</Button>
      </Form>
      {selectedPokemon ? <PokeCard pokemon={selectedPokemon} /> : null}

      <Button variant="primary" onClick={() => setModalShow(true)}>
        Launch vertically centered modal
      </Button>
      <MyModal show={modalShow} onHide={() => setModalShow(false)} />
      {
        // props ={
        //   show: modalShow,
        //   onHide: setModalShow(false)
        // }
      }
    </>
  );
}

export default App;