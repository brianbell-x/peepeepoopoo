# Revised Project Plan: ModStudio.ai

## Concept
A sleek, automotive-themed web application enabling car enthusiasts to upload images of their cars and desired modification parts (wheels, spoilers, wraps, etc.). Using GPT-4o, the app visually renders realistic modifications directly on the user's car images.

## Target User Experience
1. User arrives at the visually appealing and sleekly themed landing page.
2. User uploads an image of their car via intuitive drag-and-drop or click-to-upload interface.
3. User uploads an image of the desired car part through a similar upload interface.
4. User clicks the "Visualize Mod" button, initiating processing.
5. Clear automotive-themed loading indicator displays during image processing.
6. Final generated image showcasing the modification is elegantly presented to the user.

## Core Components

### Frontend (Next.js, Tailwind CSS, Shadcn)
- **Architecture:** Next.js App Router for efficient routing and server components.
- **UI Design Principles:**
  - Sleek, minimalist, automotive-inspired design using dark mode, carbon fiber textures, and red/white accents.
  - Mobile-first responsive layout (single-column mobile, optimized two-column desktop).
- **Layout:**
  - Prominent header with logo and tagline: "Visualize Car Modifications with AI."
  - Clearly defined and intuitive upload zones:
    - "Upload Your Car Image"
    - "Upload the Part Image"
  - Interactive upload zones with visual feedback and thumbnail previews.
  - Distinctive "Visualize Mod" button with clear disabled/enabled states.
  - Result display area using a visually appealing `Card` component, displaying generated results or relevant error messages.
- **Components:**
  - Reusable `<UploadZone label="..." onFileChange={...} />` components for uploads.
  - Icons from `lucide-react` for clarity within upload zones.
  - `Card`, `Button`, and `Label` components imported via the latest stable `shadcn` CLI.
- **Logic:**
  - Centralized state management for files, previews, loading states, results, and errors using React Hooks (`useState`, `useReducer`).
  - Robust drag-and-drop and click-to-upload functionality.
  - API integration via POST request to backend endpoint.

### Backend (FastAPI, Python 3.10+)
- **API Endpoint:** `/generate` POST route handling multipart form data (car image, part image).
- **GPT-4o Integration:**
  - Dedicated module (`client.py`) handling OpenAI API interactions.
  - Utilizes latest official OpenAI Python library.
  - Multimodal input handling as per OpenAI documentation.
  - Automotive-specific prompts optimized for realistic renderings (e.g., "show me what these wheels look like on my car—white background, car-show style image").
- **Processing:** Manages request parsing, GPT-4o call orchestration, and returning generated images.
- **Security & Management:** Environment variables for API keys. Python dependency management via Poetry.

## AI Model (GPT-4o via OpenAI API)
- Core visualization rendering engine.
- Uses latest model ID and methods specified by OpenAI.

## Project Structure

```
├── /frontend
│   ├── /app
│   ├── /components
│   ├── /public
│   ├── package.json
│   ├── pnpm-lock.yaml
│   ├── next.config.mjs
│   ├── tailwind.config.js
│   └── postcss.config.js
├── /backend
│   ├── /app
│   │   ├── main.py
│   │   └── client.py
│   ├── pyproject.toml
│   ├── poetry.lock
│   └── Dockerfile
├── .gitignore
├── README.md
└── idea.md
```

## Development Environment & Tooling
- **Frontend:** Node.js LTS, Tailwind CSS, Shadcn UI, ESLint, Prettier, pnpm/yarn.
- **Backend:** Python 3.10+, FastAPI, Poetry, Ruff, Black.
- **Containerization:** Docker for consistent development and deployment environments.

## Notes
- Emphasize clean and robust implementation.
- Extensive validation for image uploads and API interactions.
- Regular dependency updates for security and feature enhancements.

## Technology Choices Summary
- **Frontend Framework:** Next.js (App Router)
- **Backend Framework:** FastAPI
- **Runtime:** Node.js LTS, Python
- **Styling:** Tailwind CSS
- **UI Components:** Shadcn (latest CLI)
- **AI Integration:** GPT-4o via official OpenAI API
- **Package Managers:** pnpm/yarn (Frontend), Poetry (Backend)
- **ASGI Server:** Uvicorn

