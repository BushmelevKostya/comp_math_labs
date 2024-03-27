import React from 'react';
import ReactDOM from 'react-dom/client';
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import './styles/index.css';
import Main from './routes/Main';

const App = () => {
    const determineStylesheet = () => {
        return 'styles/index.css';
    };
    const router = createBrowserRouter([
        {
            path: '/',
            element: <Main/>,
        }
    ]);
    return (
        <React.StrictMode>
            <link rel="stylesheet" type="text/css" href={determineStylesheet()} />
            <RouterProvider router={router}/>
        </React.StrictMode>
    );
};
ReactDOM.createRoot(document.getElementById('root')).render(
    <App/>
)