import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';

const LibraryPage = () => {
    const { token, isAuthenticated } = useAuth();
    const navigate = useNavigate();
    const [library, setLibrary] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [removalMessage, setRemovalMessage] = useState('');

    useEffect(() => {
        // Redirect if not authenticated
        if (!isAuthenticated) {
            navigate('/login');
            return;
        }

        const fetchLibrary = async () => {
            try {
                const response = await apiService.getUserLibrary(token);
                const data = await response.json();
                console.log('Library data:', data);
                setLibrary(data);
            } catch (err) {
                console.error('Error fetching library:', err);
                setError('Failed to load library');
            } finally {
                setLoading(false);
            }
        };

        fetchLibrary();
    }, [token, isAuthenticated, navigate]);

    const handleRemoveFromLibrary = async (gameId) => {
        try {
            const response = await apiService.removeFromLibrary(gameId, token);
            if (response.ok) {
                setLibrary(library.filter(item => item.game.id !== gameId));
                setRemovalMessage('Game removed from library');
                setTimeout(() => setRemovalMessage(''), 3000); // Clear message after 3 seconds
            } else {
                setError('Failed to remove game from library');
            }
        } catch (err) {
            console.error('Error removing game:', err);
            setError('Failed to remove game from library');
        }
    };

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="max-w-6xl mx-auto px-4">
                <h1 className="text-4xl font-bold text-white mb-8">My Library</h1>
                
                {error && (
                    <div className="bg-red-500 text-white p-4 rounded mb-4">
                        {error}
                    </div>
                )}

                {removalMessage && (
                    <div className="bg-green-500 text-white p-4 rounded mb-4">
                        {removalMessage}
                    </div>
                )}

                {library.length === 0 ? (
                    <div className="text-center text-gray-400 py-12">
                        <p className="text-xl mb-4">Your library is empty</p>
                        <p>Start adding games to build your collection!</p>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {library.map(item => (
                            <div key={item.id} className="bg-gray-800 rounded-lg overflow-hidden shadow-lg">
                                <img 
                                    src={item.game.image_url || '/placeholder-game.jpg'}
                                    alt={item.game.title}
                                    className="w-full h-48 object-cover"
                                />
                                <div className="p-4">
                                    <h3 className="text-xl font-bold text-white mb-2">
                                        {item.game.title}
                                    </h3>
                                    <p className="text-gray-400 mb-4">
                                        {item.game.genre}
                                    </p>
                                    <div className="flex justify-between items-center">
                                        <button
                                            onClick={() => navigate(`/game/${item.game.id}`)}
                                            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                                        >
                                            View Details
                                        </button>
                                        <button
                                            onClick={() => handleRemoveFromLibrary(item.game.id)}
                                            className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
                                        >
                                            Remove
                                        </button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default LibraryPage;