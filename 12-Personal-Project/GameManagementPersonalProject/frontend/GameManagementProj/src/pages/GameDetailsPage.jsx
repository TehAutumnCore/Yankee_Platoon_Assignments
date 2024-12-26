import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';

const GameDetailsPage = () => {
    const { id } = useParams();
    const { token, isAuthenticated, user } = useAuth();
    const [game, setGame] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [addingToLibrary, setAddingToLibrary] = useState(false);
    const [libraryMessage, setLibraryMessage] = useState('');
    const [isInLibrary, setIsInLibrary] = useState(false);
    const [reviews, setReviews] = useState([]);
    const [newReview, setNewReview] = useState({ review_text: '', rating: 5 });
    const [reviewError, setReviewError] = useState('');

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

    useEffect(() => {
        const fetchReviews = async () => {
            try {
                if (token) {
                    const response = await apiService.getGameReviews(id, token);
                    const data = await response.json();
                    setReviews(data);
                }
            } catch (err) {
                console.error('Error fetching reviews:', err);
            }
        };

        if (game && isAuthenticated) {
            fetchReviews();
        }
    }, [id, game, token, isAuthenticated]);

    useEffect(() => {
        const checkLibraryStatus = async () => {
            if (isAuthenticated && token) {
                try {
                    const response = await apiService.getUserLibrary(token);
                    const libraryData = await response.json();
                    setIsInLibrary(libraryData.some(item => item.game.id === parseInt(id)));
                } catch (err) {
                    console.error('Error checking library status:', err);
                }
            }
        };

        checkLibraryStatus();
    }, [id, isAuthenticated, token]);

    const handleLibraryAction = async () => {
        if (!isAuthenticated) {
            setLibraryMessage('Please log in to add games to your library');
            return;
        }

        setAddingToLibrary(true);
        try {
            if (isInLibrary) {
                const response = await apiService.removeFromLibrary(game.id, token);
                if (response.ok) {
                    setIsInLibrary(false);
                    setLibraryMessage('Game removed from library!');
                }
            } else {
                const response = await apiService.addToLibrary(game.id, token);
                if (response.ok) {
                    setIsInLibrary(true);
                    setLibraryMessage('Game added to library!');
                }
            }
        } catch (err) {
            console.error('Error updating library:', err);
            setLibraryMessage('Failed to update library');
        } finally {
            setAddingToLibrary(false);
        }
    };

    const handleReviewSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log('Submitting review for game:', id);
            const reviewData = {
                review_text: newReview.review_text,
                rating: newReview.rating
            };
            
            const response = await apiService.createReview(id, reviewData, token);
            if (response.ok) {
                const data = await response.json();
                console.log('Review submitted successfully:', data);
                setReviews([...reviews, data]);
                setNewReview({ review_text: '', rating: 5 });
                setReviewError('');
                // Refresh reviews
                const updatedReviewsResponse = await apiService.getGameReviews(id, token);
                const updatedReviews = await updatedReviewsResponse.json();
                setReviews(updatedReviews);
            } else {
                const errorData = await response.json();
                console.error('Review submission failed:', errorData);
                setReviewError(errorData.error || 'Failed to submit review');
            }
        } catch (err) {
            console.error('Error submitting review:', err);
            setReviewError('Failed to submit review');
        }
    };

    const handleDeleteReview = async (reviewId) => {
        try {
            const response = await apiService.deleteReview(reviewId, token);
            if (response.ok) {
                setReviews(reviews.filter(review => review.id !== reviewId));
            }
        } catch (err) {
            console.error('Error deleting review:', err);
        }
    };

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
                <div className="text-white text-xl">
                    {error || 'Game not found'}
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="max-w-6xl mx-auto px-4">
                <div className="bg-gray-800 rounded-lg overflow-hidden shadow-xl">
                    <img
                        src={game.image_url || '/placeholder-game.jpg'}
                        alt={game.title}
                        className="w-full h-96 object-cover"
                    />

                    <div className="p-6">
                        <div className="flex justify-between items-start">
                            <div>
                                <h1 className="text-4xl font-bold text-white mb-2">
                                    {game.title}
                                </h1>
                                <p className="text-gray-400 text-lg mb-4">
                                    {game.genre}
                                </p>
                            </div>
                            <div className="text-right">
                                <div className="text-3xl text-green-500 font-bold">
                                    ${game.price}
                                </div>
                                {game.sale && (
                                    <span className="bg-red-500 text-white px-3 py-1 rounded text-sm ml-2">
                                        On Sale!
                                    </span>
                                )}
                            </div>
                        </div>

                        <div className="mt-6">
                            <h2 className="text-xl font-bold text-white mb-2">
                                About This Game
                            </h2>
                            <p className="text-gray-300 leading-relaxed">
                                {game.description}
                            </p>
                        </div>

                        <div className="mt-8">
                            {libraryMessage && (
                                <div className={`mb-4 p-3 rounded ${
                                    libraryMessage.includes('Failed') || libraryMessage.includes('Please log in')
                                        ? 'bg-red-500'
                                        : 'bg-green-500'
                                } text-white`}>
                                    {libraryMessage}
                                </div>
                            )}
                            <div className="flex gap-4">
                                <a 
                                    href={`https://store.steampowered.com/app/${game.steam_app_id}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                                >
                                    View on Steam
                                </a>
                                <button 
                                    onClick={handleLibraryAction}
                                    disabled={addingToLibrary}
                                    className={`${
                                        addingToLibrary 
                                            ? 'bg-gray-400 cursor-not-allowed' 
                                            : isInLibrary
                                                ? 'bg-red-600 hover:bg-red-700'
                                                : 'bg-green-600 hover:bg-green-700'
                                    } text-white px-6 py-2 rounded`}
                                >
                                    {addingToLibrary 
                                        ? 'Processing...' 
                                        : isInLibrary 
                                            ? 'Remove from Library' 
                                            : 'Add to Library'}
                                </button>
                            </div>
                        </div>

                        {/* Reviews Section */}
                        <div className="mt-12">
                            <h2 className="text-2xl font-bold text-white mb-6">Reviews</h2>
                            
                            {isAuthenticated ? (
                                <form onSubmit={handleReviewSubmit} className="mb-8">
                                    <div className="mb-4">
                                        <label className="block text-white mb-2">Rating</label>
                                        <select
                                            value={newReview.rating}
                                            onChange={(e) => setNewReview({...newReview, rating: parseInt(e.target.value)})}
                                            className="w-full p-2 rounded bg-gray-700 text-white"
                                        >
                                            {[5,4,3,2,1].map(num => (
                                                <option key={num} value={num}>{num} Stars</option>
                                            ))}
                                        </select>
                                    </div>
                                    <div className="mb-4">
                                        <label className="block text-white mb-2">Your Review</label>
                                        <textarea
                                            value={newReview.review_text}
                                            onChange={(e) => setNewReview({...newReview, review_text: e.target.value})}
                                            className="w-full p-2 rounded bg-gray-700 text-white h-32"
                                            placeholder="Write your review here..."
                                            required
                                        />
                                    </div>
                                    {reviewError && (
                                        <div className="mb-4 text-red-500">
                                            {reviewError}
                                        </div>
                                    )}
                                    <button 
                                        type="submit"
                                        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                                    >
                                        Submit Review
                                    </button>
                                </form>
                            ) : (
                                <p className="text-gray-400 mb-6">Please log in to submit a review.</p>
                            )}

                            <div className="space-y-6">
                                {reviews.length > 0 ? (
                                    reviews.map(review => (
                                        <div key={review.id} className="bg-gray-800 p-4 rounded">
                                            <div className="flex justify-between items-start">
                                                <div>
                                                    <div className="text-yellow-500 text-lg mb-2">
                                                        {'★'.repeat(review.rating)}{'☆'.repeat(5-review.rating)}
                                                    </div>
                                                    <p className="text-gray-300">{review.review_text}</p>
                                                </div>
                                                {isAuthenticated && review.user === user?.id && (
                                                    <button
                                                        onClick={() => handleDeleteReview(review.id)}
                                                        className="text-red-500 hover:text-red-700"
                                                    >
                                                        Delete
                                                    </button>
                                                )}
                                            </div>
                                        </div>
                                    ))
                                ) : (
                                    <p className="text-gray-400">No reviews yet. Be the first to review!</p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default GameDetailsPage;