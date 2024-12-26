import { Link } from "react-router-dom";
import { useAuth } from '../../contexts/AuthContext';

const NavBar = () => {
    const { isAuthenticated, logout, user } = useAuth();

    return (
        <nav className="bg-gray-800 p-4">
            <div className="container mx-auto flex justify-between items-center">
                <Link to="/" className="text-white text-xl font-bold">
                    Game Management
                </Link>
                <div className="flex gap-4 items-center">
                    {isAuthenticated ? (
                        <>
                            <span className="text-gray-300">Welcome, {user?.display_name}</span>
                            <Link to="/library" className="text-white hover:text-gray-300">
                                Library
                            </Link>
                            <Link to="/profile" className="text-white hover:text-gray-300">
                                Profile
                            </Link>
                            <button 
                                onClick={logout}
                                className="text-white hover:text-gray-300"
                            >
                                Logout
                            </button>
                        </>
                    ) : (
                        <>
                            <Link to="/login" className="text-white hover:text-gray-300">
                                Login
                            </Link>
                            <Link to="/signup" className="text-white hover:text-gray-300">
                                Sign Up
                            </Link>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
};

export default NavBar;