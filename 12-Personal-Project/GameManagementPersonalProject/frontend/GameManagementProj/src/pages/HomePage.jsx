import { useState } from 'react';
import GameCarousel from '../components/GameCarousel';

const HomePage = () => {
    const [games] = useState({
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
        ],
        adventure: [
            {
                id: 3,
                title: "Test Game 3",
                genre: "Adventure",
                price: 39.99,
                sale: true,
                image_url: "https://placehold.co/600x400"
            }
        ]
    });

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