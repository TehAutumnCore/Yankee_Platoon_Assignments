import { useState, useEffect } from 'react';
import GameCarousel from '../components/GameCarousel';
import { apiService } from '../services/api';

const HomePage = () => {
    const [games, setGames] = useState({
        action: []
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchGames = async () => {
            try {
                console.log('Fetching games...');
                const response = await apiService.getAllGames();
                console.log('API Response:', response);
                const data = await response.json();
                console.log('Games data:', data);
                
                // Keep your test data as a fallback
                const groupedGames = {
                    action: data.length > 0 ? data : [
                        {
                            id: 1,
                            title: "Test Game 1",
                            genre: "Action",
                            price: 59.99,
                            sale: true,
                            image_url: "https://placehold.co/600x400"
                        },
                        {
                            id: 2,
                            title: "Test Game 2",
                            genre: "Action",
                            price: 49.99,
                            sale: false,
                            image_url: "https://placehold.co/600x400"
                        }
                    ]
                };
                
                console.log('Grouped games:', groupedGames);
                setGames(groupedGames);
            } catch (err) {
                console.error('Error fetching games:', err);
                // Fall back to test data if API fails
                setGames({
                    action: [
                        {
                            id: 1,
                            title: "Test Game 1",
                            genre: "Action",
                            price: 59.99,
                            sale: true,
                            image_url: "https://placehold.co/600x400"
                        },
                        {
                            id: 2,
                            title: "Test Game 2",
                            genre: "Action",
                            price: 49.99,
                            sale: false,
                            image_url: "https://placehold.co/600x400"
                        }
                    ]
                });
            } finally {
                setLoading(false);
            }
        };

        fetchGames();
    }, []);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-screen bg-gray-900">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <section className="max-w-screen-xl mx-auto">
                <h1 className="text-4xl font-bold text-white mb-8 px-4">Welcome to Game Management</h1>
                
                {Object.entries(games).map(([genre, gameList]) => (
                    gameList.length > 0 && (
                        <GameCarousel 
                            key={genre} 
                            title={genre.charAt(0).toUpperCase() + genre.slice(1)} 
                            games={gameList} 
                        />
                    )
                ))}
            </section>
        </div>
    );
};

export default HomePage;