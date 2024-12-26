import { useState } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';

const GameCard = ({ game, inLibrary }) => {
    const { token, isAuthenticated } = useAuth();
    const [removing, setRemoving] = useState(false);

    const handleRemoveFromLibrary = async () => {
        if (!isAuthenticated) return;

        setRemoving(true);
        try {
            const response = await apiService.removeFromLibrary(game.id, token);
            if (response.ok) {
                window.location.reload(); // Refresh the library page
            }
        } catch (err) {
            console.error('Error removing from library:', err);
        } finally {
            setRemoving(false);
        }
    };

    return (
        <div className="w-64 bg-gray-800 rounded-lg overflow-hidden shadow-lg">
            <img 
                src={game.image_url || '/placeholder-game.jpg'} 
                alt={game.title}
                className="w-full h-36 object-cover"
            />
            <div className="p-4">
                <h3 className="text-lg font-semibold text-white">{game.title}</h3>
                <p className="text-gray-400 text-sm">{game.genre}</p>
                <div className="mt-2 flex justify-between items-center">
                    <span className="text-green-500">${game.price}</span>
                    {game.sale && (
                        <span className="bg-red-500 px-2 py-1 rounded text-sm text-white">
                            On Sale!
                        </span>
                    )}
                </div>
                <div className="mt-4 flex flex-col gap-2">
                    <Link 
                        to={`/game/${game.id}`}
                        className="block bg-blue-600 text-white text-center px-4 py-2 rounded hover:bg-blue-700"
                    >
                        View Details
                    </Link>
                    {inLibrary && (
                        <button 
                            onClick={handleRemoveFromLibrary}
                            disabled={removing}
                            className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 disabled:bg-gray-500"
                        >
                            {removing ? 'Removing...' : 'Remove from Library'}
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
};

GameCard.propTypes = {
    game: PropTypes.shape({
        id: PropTypes.number.isRequired,
        title: PropTypes.string.isRequired,
        genre: PropTypes.string,
        price: PropTypes.number,
        sale: PropTypes.bool,
        image_url: PropTypes.string,
    }).isRequired,
    inLibrary: PropTypes.bool
};

GameCard.defaultProps = {
    inLibrary: false
};

export default GameCard;