import { useRouteError, Link } from 'react-router-dom';

const ErrorPage = () => {
    const error = useRouteError();

    return (
        <div className="min-h-screen bg-gray-900 flex items-center justify-center">
            <div className="text-center">
                <h1 className="text-6xl font-bold text-red-500 mb-4">Oops!</h1>
                <p className="text-xl text-gray-400 mb-4">
                    Sorry, an unexpected error has occurred.
                </p>
                <p className="text-gray-500 mb-8">
                    {error.statusText || error.message}
                </p>
                <Link 
                    to="/" 
                    className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                >
                    Return Home
                </Link>
            </div>
        </div>
    );
};

export default ErrorPage;