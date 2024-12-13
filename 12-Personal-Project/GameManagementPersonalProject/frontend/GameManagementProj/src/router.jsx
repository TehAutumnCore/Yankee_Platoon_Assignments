import HomePage from "./pages/Homepage.jsx";
import LibraryPage from "./pages/LibraryPage.jsx";
import ProfilePage from "./pages/ProfilePage.jsx";
import AboutMePage from "./pages/AboutMePage.jsx";
import LogInPage from "./pages/LogInPage.jsx";
import SignUpPage from "./pages/SignUpPage.jsx";
import NotFoundPage from "./pages/NotFoundPage.jsx";
import ErrorPage from "./pages/ErrorPage.jsx";
import App from "./App"
import {createBrowserRouter} from "react-router-dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <HomePage/>
            },
            {
                path: "library/",
                element:<LibraryPage/>,
            },
            {
                path: "profile/",
                element:<ProfilePage/>,
            },
            {
                path: "aboutme/",
                element:<AboutMePage/>,
            },
            {
                path: "login/",
                element:<LogInPage/>,
            },
            {
                path: "signup/",
                element:<SignUpPage/>,
            },
            {
                path: "*",
                element:<NotFoundPage/>,
            },
        ],
        errorElement: <ErrorPage/>
    }
])

export default router