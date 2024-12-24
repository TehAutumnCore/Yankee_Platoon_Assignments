import { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';
import GameCard from '../components/GameCard';

const LibraryPage = () => {
    const { token } = useAuth();
    const [library, setLibrary] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchLibrary = async () => {
            try {
                const response = await apiService.getUserLibrary(token);
                const data = await response.json();
                setLibrary(data);
            } catch (err) {
                console.error('Error fetching library:', err);
                setError('Failed to load library');
            } finally {
                setLoading(false);
            }
        };

        fetchLibrary();
    }, [token]);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <p className="text-red-500 text-xl">{error}</p>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="max-w-screen-xl mx-auto px-4">
                <h1 className="text-4xl font-bold text-white mb-8">My Library</h1>
                
                {library.length === 0 ? (
                    <p className="text-white text-xl">Your library is empty</p>
                ) : (
                    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                        {library.map(item => (
                            <GameCard key={item.id} game={item.game} />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default LibraryPage;