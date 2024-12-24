import PropTypes from 'prop-types';
import GameCard from './GameCard';

const GameCarousel = ({ title, games }) => {
    return (
        <div className="mb-8">
            <h2 className="text-2xl font-bold text-white mb-4 px-4">{title}</h2>
            <div className="relative">
                <div className="flex overflow-x-auto gap-4 px-4 pb-4">
                    {games.map(game => (
                        <GameCard key={game.id} game={game} />
                    ))}
                </div>
            </div>
        </div>
    );
};

GameCarousel.propTypes = {
    title: PropTypes.string.isRequired,
    games: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            title: PropTypes.string.isRequired,
            genre: PropTypes.string,
            price: PropTypes.number,
            sale: PropTypes.bool,
            image_url: PropTypes.string,
        })
    ).isRequired
};

export default GameCarousel;