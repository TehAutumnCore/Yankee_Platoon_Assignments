const API_URL = 'http://localhost:8000/api/v1';

export const apiService = {
    // Auth endpoints
    login: (credentials) => fetch(`${API_URL}/users/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
    }),

    register: (userData) => fetch(`${API_URL}/users/signup/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
    }),

    // User endpoints
    getUserInfo: (token) => fetch(`${API_URL}/users/info/`, {
        headers: {
            'Authorization': `Token ${token}`
        }
    }),

    updateUserInfo: (token, userData) => fetch(`${API_URL}/users/info/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({
            display_name: userData.display_name,
            age: parseInt(userData.age)
        })
    }),

    // Game endpoints
    getAllGames: () => fetch(`${API_URL}/games/`),
    
    getGameById: (id) => fetch(`${API_URL}/games/${id}/`),

    // Library endpoints
    getUserLibrary: (token) => fetch(`${API_URL}/library/`, {
        headers: { 
            'Authorization': `Token ${token}` 
        }
    }),

    addToLibrary: (gameId, token) => fetch(`${API_URL}/library/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({ game: gameId })
    }),

    removeFromLibrary: (gameId, token) => fetch(`${API_URL}/library/${gameId}/delete/`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Token ${token}`
        }
    }),

    // Review endpoints
    getGameReviews: (gameId, token) => fetch(`${API_URL}/reviews/game/${gameId}/`, {
        headers: {
            'Authorization': `Token ${token}`
        }
    }),

    createReview: (gameId, reviewData, token) => fetch(`${API_URL}/reviews/game/${gameId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({
            review_text: reviewData.review_text,
            rating: reviewData.rating
        })
    }),

    deleteReview: (reviewId, token) => fetch(`${API_URL}/reviews/${reviewId}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Token ${token}`
        }
    })
};