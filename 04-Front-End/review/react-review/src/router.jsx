import {createBrowserRouter} from "react-router-dom"
import App from "./App"
import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage'
import CharactersPage from './pages/CharactersPage'
import ErrorPage from './pages/ErrorPage'
import NotFoundPage from './pages/NotFoundPage'


const router = createBrowserRouter([
    {
    path:'/',
    element:<App/>,
    children: [
        {
            index: true,
            element: <HomePage/>,
        },
        {
            path:'/about/',
            element:<AboutPage/>
        },
        {
            path:'/characters/',
            element: <CharactersPage/>
        },
        {
            path: "*",
            element: <NotFoundPage/>
        },
    ],
    errorElement: <ErrorPage/>
    }
])

export default router