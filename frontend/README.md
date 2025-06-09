# Deep Research Frontend

This directory contains the React web interface for the Deep Research project. The application is built with **Vite**, **TypeScript**, and **Tailwind CSS**.

## Getting Started

Install dependencies and start a development server:

```bash
cd frontend
npm install
npm run dev
```

The app will be served on <http://localhost:5173> by default.

### Environment Variables

Configuration is handled through environment variables that start with `RESEARCH_`. Copy `.env.example` to `.env` and adjust the values for your environment:

```bash
cp .env.example .env
# edit .env to point to your backend
```

The `RESEARCH_API_URL` variable controls which backend endpoint the frontend uses.

## Building for Production

To generate a production build run:

```bash
npm run build
```

You can preview the build locally with:

```bash
npm run preview
```

## Project Structure

Key files and folders inside `frontend/`:

```
public/           Static assets and `index.html`
src/              Application source code
  components/     Reusable UI elements
  pages/          Route components
  hooks/          Custom React hooks
  lib/            API helpers and utilities
  styles/         Global stylesheets
  App.tsx         Main application component
  main.tsx        Entry point that mounts `App`
```

Additional configuration files include `tsconfig.json`, `tailwind.config.js` and `vite.config.ts`.
