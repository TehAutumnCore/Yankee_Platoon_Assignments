import Card from 'react-bootstrap/Card';

function PokeCard({pokemon}) {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={pokemon.sprites.front_default} />
      <Card.Body>
        <Card.Title>{pokemon.name}</Card.Title>
      </Card.Body>
    </Card>
  );
}

export default PokeCard;