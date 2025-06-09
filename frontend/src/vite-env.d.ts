/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly RESEARCH_API_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
