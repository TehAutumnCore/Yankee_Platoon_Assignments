const API_URL = 'http://localhost:8000/api/v1';

export const apiService = {
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

    getAllGames: () => fetch(`${API_URL}/games/`),
    getGameById: (id) => fetch(`${API_URL}/games/${id}/`),
    
    getUserLibrary: (token) => fetch(`${API_URL}/library/`, {
        headers: { 'Authorization': `Token ${token}` }
    }),
    
    addToLibrary: (gameId, token) => fetch(`${API_URL}/library/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        },
        body: JSON.stringify({ game: gameId })
    })
};