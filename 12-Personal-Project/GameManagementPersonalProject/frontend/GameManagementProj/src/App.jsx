import { Outlet } from 'react-router-dom';
import NavBar from './components/layout/NavBar';
import Footer from './components/layout/Footer';

function App() {
    return (
        <div className="flex flex-col min-h-screen bg-gray-900">
            <NavBar />
            <main className="flex-grow">
                <Outlet />
            </main>
            <Footer />
        </div>
    );
}

export default App;