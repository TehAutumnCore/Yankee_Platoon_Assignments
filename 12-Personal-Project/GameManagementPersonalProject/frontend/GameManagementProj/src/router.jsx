import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import LibraryPage from "./pages/LibraryPage";
import ProfilePage from "./pages/ProfilePage";
import AboutMePage from "./pages/AboutMePage";
import GameDetailsPage from "./pages/GameDetailsPage";
import LogInPage from "./pages/LogInPage";
import SignUpPage from "./pages/SignUpPage";
import NotFoundPage from "./pages/NotFoundPage";
import ErrorPage from "./pages/ErrorPage";
import AuthRequired from "./components/AuthRequired";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "library/",
                element: (
                    <AuthRequired>
                        <LibraryPage />
                    </AuthRequired>
                ),
            },
            {
                path: "profile/",
                element: (
                    <AuthRequired>
                        <ProfilePage />
                    </AuthRequired>
                ),
            },
            {
                path: "game/:id",
                element: <GameDetailsPage />,
            },
            {
                path: "aboutme/",
                element: <AboutMePage />,
            },
            {
                path: "login/",
                element: <LogInPage />,
            },
            {
                path: "signup/",
                element: <SignUpPage />,
            },
            {
                path: "*",
                element: <NotFoundPage />,
            },
        ],
        errorElement: <ErrorPage />
    }
]);

export default router;