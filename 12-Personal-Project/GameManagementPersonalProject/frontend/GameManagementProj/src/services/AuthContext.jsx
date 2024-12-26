import PropTypes from 'prop-types';
import { createContext, useState, useContext } from 'react';
import { apiService } from '../services/api';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [token, setToken] = useState(localStorage.getItem('token'));
    const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')));  // Add this line

    const login = async (email, password) => {
        try {
            const response = await apiService.login({ email, password });
            const data = await response.json();
            
            if (response.ok) {
                localStorage.setItem('token', data.token);
                localStorage.setItem('user', JSON.stringify(data.user));  // Add this line
                setToken(data.token);
                setUser(data.user);
                return { success: true };
            }
            return { success: false, error: data.error || 'Login failed' };
        } catch (err) {
            console.error('Login error:', err);
            return { success: false, error: 'Login failed' };
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('user');  // Add this line
        setToken(null);
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, token, login, logout, isAuthenticated: !!token }}>
            {children}
        </AuthContext.Provider>
    );
};

AuthProvider.propTypes = {
    children: PropTypes.node.isRequired
};

export const useAuth = () => useContext(AuthContext);