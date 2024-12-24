import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { apiService } from '../services/api';

const GameDetailsPage = () => {
    const { id } = useParams();
    const [game, setGame] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchGameDetails = async () => {
            try {
                const response = await apiService.getGameById(id);
                const data = await response.json();
                setGame(data);
            } catch (err) {
                console.error('Error fetching game details:', err);
                setError('Failed to load game details');
            } finally {
                setLoading(false);
            }
        };

        fetchGameDetails();
    }, [id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
            </div>
        );
    }

    if (error || !game) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <p className="text-red-500 text-xl">{error || 'Game not found'}</p>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="max-w-4xl mx-auto px-4">
                <div className="bg-gray-800 rounded-lg overflow-hidden shadow-xl">
                    <img 
                        src={game.image_url || '/placeholder-game.jpg'} 
                        alt={game.title}
                        className="w-full h-64 object-cover"
                    />
                    
                    <div className="p-6">
                        <h1 className="text-3xl font-bold text-white mb-4">{game.title}</h1>
                        
                        <div className="flex items-center gap-4 mb-4">
                            <span className="text-gray-400">{game.genre}</span>
                            <span className="text-green-500 text-xl">${game.price}</span>
                            {game.sale && (
                                <span className="bg-red-500 px-3 py-1 rounded text-white">
                                    On Sale!
                                </span>
                            )}
                        </div>

                        <p className="text-gray-300 mb-6">{game.description}</p>

                        <div className="flex gap-4">
                            <a 
                                href={`https://store.steampowered.com/app/${game.steam_app_id}`}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                            >
                                View on Steam
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default GameDetailsPage;