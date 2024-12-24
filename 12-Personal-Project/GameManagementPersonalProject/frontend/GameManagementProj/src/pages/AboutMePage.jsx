const AboutMePage = () => {
    return (
        <div className="min-h-screen bg-gray-900 py-8">
            <div className="max-w-3xl mx-auto px-4">
                <h1 className="text-4xl font-bold text-white mb-6">About This Project</h1>
                
                <div className="bg-gray-800 rounded-lg p-6 shadow-xl">
                    <section className="mb-8">
                        <h2 className="text-2xl font-bold text-white mb-4">Overview</h2>
                        <p className="text-gray-300">
                            This Game Management project is a fullstack application built with React and Django,
                            integrating with Steam and Twitch APIs to provide a comprehensive gaming platform.
                        </p>
                    </section>

                    <section className="mb-8">
                        <h2 className="text-2xl font-bold text-white mb-4">Features</h2>
                        <ul className="list-disc list-inside text-gray-300 space-y-2">
                            <li>Browse and search games from Steam</li>
                            <li>Create and manage your game library</li>
                            <li>View game details and current prices</li>
                            <li>Watch related Twitch streams</li>
                            <li>Write and manage game reviews</li>
                        </ul>
                    </section>

                    <section>
                        <h2 className="text-2xl font-bold text-white mb-4">Technologies Used</h2>
                        <ul className="list-disc list-inside text-gray-300 space-y-2">
                            <li>Frontend: React, Tailwind CSS</li>
                            <li>Backend: Django, Django REST Framework</li>
                            <li>Database: PostgreSQL</li>
                            <li>APIs: Steam Web API, Twitch API</li>
                        </ul>
                    </section>
                </div>
            </div>
        </div>
    );
};

export default AboutMePage;