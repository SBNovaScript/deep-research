import React from 'react';
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router';
import Home from './pages/Home';
import Results from './pages/Results';

const router = createBrowserRouter([
  { path: '/', element: <Home /> },
  { path: '/task/:id', element: <Results /> },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
