import { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { apiService } from '../services/api';

const ProfilePage = () => {
    const { token } = useAuth();
    const [profileData, setProfileData] = useState({
        email: '',
        display_name: '',
        age: ''
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await apiService.getUserInfo(token);
                const data = await response.json();
                setProfileData(data);
            } catch (err) {
                console.error('Error fetching profile:', err);
                setError('Failed to load profile');
            } finally {
                setLoading(false);
            }
        };

        fetchProfile();
    }, [token]);

    const handleChange = (e) => {
        setProfileData({
            ...profileData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await apiService.updateUserInfo(token, profileData);
            if (response.ok) {
                setMessage('Profile updated successfully');
            } else {
                setError('Failed to update profile');
            }
        } catch (err) {
            console.error('Error updating profile:', err);
            setError('Failed to update profile');
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
            <div className="max-w-md mx-auto bg-gray-800 rounded-lg shadow-xl p-8">
                <h1 className="text-3xl font-bold text-white mb-6">Profile</h1>
                
                {error && <p className="text-red-500 mb-4">{error}</p>}
                {message && <p className="text-green-500 mb-4">{message}</p>}
                
                <form onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label className="block text-white mb-2">Email</label>
                        <input 
                            type="email"
                            name="email"
                            value={profileData.email}
                            onChange={handleChange}
                            className="w-full p-2 rounded bg-gray-700 text-white"
                            disabled
                        />
                    </div>

                    <div className="mb-4">
                        <label className="block text-white mb-2">Display Name</label>
                        <input 
                            type="text"
                            name="display_name"
                            value={profileData.display_name}
                            onChange={handleChange}
                            className="w-full p-2 rounded bg-gray-700 text-white"
                        />
                    </div>

                    <div className="mb-6">
                        <label className="block text-white mb-2">Age</label>
                        <input 
                            type="number"
                            name="age"
                            value={profileData.age}
                            onChange={handleChange}
                            min="18"
                            className="w-full p-2 rounded bg-gray-700 text-white"
                        />
                    </div>

                    <button 
                        type="submit"
                        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
                    >
                        Update Profile
                    </button>
                </form>
            </div>
        </div>
    );
};

export default ProfilePage;