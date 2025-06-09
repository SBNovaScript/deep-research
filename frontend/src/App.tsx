import React from 'react';
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router';
import Home from './pages/Home';
import Results from './pages/Results';
import RootLayout from './components/RootLayout';

const router = createBrowserRouter([
  {
    path: '/',
    Component: RootLayout,
    children: [
      { index: true, Component: Home },
      { path: 'task/:id', Component: Results },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
