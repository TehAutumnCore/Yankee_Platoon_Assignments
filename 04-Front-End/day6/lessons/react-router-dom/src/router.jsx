import { useState } from 'react'
import App from './App.jsx'
import AboutPage from './pages/AboutPage.jsx'
import ContactPage from './pages/ContactPage'
import HomePage from './pages/HomePage'
import {createBrowserRouter} from "react-router-dom";
import YankeePage from './pages/YankeePage.jsx'
import GaryPage from './pages/GaryPage.jsx'
import NotFoundPage from './pages/NotFoundPage.jsx'
import ErrorPage from './pages/ErrorPage.jsx'

const router = createBrowserRouter([
    {
        path:'/',
        element: <App/>,
        children:[
            {
                index:true,
                element:<HomePage/>
            },
            {
                path:"about/",
                element:<AboutPage/>
            },
            {
                path:"contact",
                element:<ContactPage/>
            },
            {
                path:"Yankee/",
                element:<YankeePage/>
            },
            {
                path:"Gary/",
                element:<GaryPage/>
            },
            {
                path:"*",
                element:<NotFoundPage/>
            }
        ],
        errorElement: <ErrorPage/>
    },
])

export default router