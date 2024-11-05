import {createBrowserRouter} from "react-router-dom"
import App from "./App"
import HomePage from "./pages/HomePage"
import CharactersPage from "./pages/CharactersPage"
import AboutPage from "./pages/AboutPage"

const router = createBrowserRouter([
    {
        path:"/",
        element:<App />,
        children: [
            {
                index:true,
                element:<HomePage/>
            },
            //{import pages}
        ]
    }
])

export default router