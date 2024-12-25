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
    const [successMessage, setSuccessMessage] = useState('');

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                console.log('Fetching profile with token:', token);
                const response = await apiService.getUserInfo(token);
                console.log('Profile response:', response);
                const data = await response.json();
                console.log('Profile data:', data);
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
        setError('');
        setSuccessMessage('');
        try {
            console.log('Sending update with data:', profileData);
            const response = await apiService.updateUserInfo(token, profileData);
            console.log('Update response status:', response.status);
            
            const data = await response.json();
            console.log('Update response data:', data);

            if (response.ok) {
                setSuccessMessage('Profile updated successfully');
            } else {
                setError(data.error || 'Failed to update profile');
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
                
                {error && (
                    <div className="bg-red-500 text-white p-3 rounded mb-4">
                        {error}
                    </div>
                )}
                
                {successMessage && (
                    <div className="bg-green-500 text-white p-3 rounded mb-4">
                        {successMessage}
                    </div>
                )}

                <form onSubmit={handleSubmit}>
                    <div className="space-y-4">
                        <div>
                            <label htmlFor="email" className="block text-white mb-2">
                                Email
                            </label>
                            <input
                                id="email"
                                name="email"
                                type="email"
                                value={profileData.email}
                                className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600"
                                disabled
                            />
                        </div>

                        <div>
                            <label htmlFor="display_name" className="block text-white mb-2">
                                Display Name
                            </label>
                            <input
                                id="display_name"
                                name="display_name"
                                type="text"
                                value={profileData.display_name}
                                onChange={handleChange}
                                className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600"
                            />
                        </div>

                        <div>
                            <label htmlFor="age" className="block text-white mb-2">
                                Age
                            </label>
                            <input
                                id="age"
                                name="age"
                                type="number"
                                min="18"
                                value={profileData.age}
                                onChange={handleChange}
                                className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600"
                            />
                        </div>
                    </div>

                    <button
                        type="submit"
                        className="mt-6 w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
                    >
                        Update Profile
                    </button>
                </form>
            </div>
        </div>
    );
};

export default ProfilePage;