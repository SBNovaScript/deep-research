# Planned Frontend Directory Layout

This repository will host a React and TypeScript application within a `frontend/` folder. The following directory structure keeps components modular and separates application concerns:

```
frontend/
  public/           # Static assets (favicon, index.html)
  src/
    components/     # Reusable UI elements
    pages/          # Top-level pages or routes
    hooks/          # Custom React hooks
    lib/            # Utility functions and shared libraries
    styles/         # Tailwind and global stylesheets
    App.tsx         # Main application component
    main.tsx        # Entry point for React
  package.json
  tsconfig.json
  tailwind.config.js
  vite.config.ts
```

This layout follows common conventions for Vite-based React projects with TypeScript and Tailwind CSS. Additional folders can be added in `src/` as the application grows (e.g. `contexts/`, `services/`).
