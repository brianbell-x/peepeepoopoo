# Project Plan: Virtual Car Part Fitter

**Concept:** A simple web application allowing users to upload an image of their car and an image of a car part (e.g., wheels, spoilers, wraps, etc), and then use GPT 4o to visualize how the part would look on the car.

**Target User Experience:**
1. User visits the application page.
2. User uploads an image of their car.
3. User uploads an image of the car part.
4. User clicks a "Generate" button.
5. A loading indicator (spinner) appears while the image is processed.
6. The application displays the generated image showing the part fitted onto the car.

**Core Components:**

1.  **Frontend (Next.js + Tailwind CSS):**
    *   **UI:** Modern, AI-centric design.
        *   Clear sections for uploading images.
        *   "Upload Car Image" button.
        *   "Upload Part Image" button.
        *   Thumbnails/previews of uploaded images (optional but good UX).
        *   "Generate Visualization" button (disabled until both images are uploaded).
        *   Loading spinner displayed during backend processing.
        *   Display area for the final generated image.
    *   **Logic:**
        *   Handles file uploads.
        *   Sends image data to the backend API upon clicking "Generate".
        *   Displays loading state.
        *   Receives and displays the generated image from the backend.

2.  **Backend (FastAPI - Python):**
    *   **API Endpoint:** A single endpoint (e.g., `/generate`) that accepts POST requests with the car image and part image data (likely base64 encoded or multipart/form-data).
    *   **GPT-4o Integration:**
        *   Contains the isolated logic for calling the GPT-4o Flash API.
        *   This logic will reside in a dedicated function/module (e.g., `GPT-4o_integration.py`) accepting image data and returning the response, following the Vertical Spine principle.
        *   Uses the prompt: `"show me what these wheels look look like on my car. - white background, car-show style image"` (Note: This prompt assumes wheels; might need adjustment for other parts later).
    *   **Processing:** Orchestrates receiving the request, calling the GPT-4o function, and returning the generated image URL or data to the frontend.
    *   **Security:** Handles API keys securely (e.g., via environment variables).

3.  **AI Model (GPT-4o):**
    *   The core engine for generating the visualization based on the provided images and prompt.

**Project Structure:**

```
/VisualizeAi
├── /frontend  (Next.js App)
│   ├── /pages
│   ├── /components
│   ├── /public
│   ├── package.json
│   └── ... (Next.js config files)
├── /backend   (FastAPI App)
│   ├── main.py
│   ├── GPT-4o_integration.py (Isolated GPT-4o API logic)
│   ├── requirements.txt
│   └── ... (FastAPI config/helper files)
├── .gitignore
├── README.md
└── idea.md (This file)

```

**Notes:**
*   Focus on a clean implementation of the core workflow first.
*   Error handling (e.g., failed uploads, API errors) should be added.
*   Consider image size/format limitations.

See GPT-4o docs at `GPT-4o_docs.md`

app ui should be really simple. can use shadcn. 

Button to upload image of parts. Button to upload image of Car. Generate button

Spinner showing that a generation is occuring.

A display area for the generated images.

Note: Use Vertical Spine Architecture for this codebase. Specifically isolate the entire api call to a single function/file with system message, messages as arguments while returning `response`. This will allow me to hot swap the api really quickly if something new comes along. 

**Technology Choices:**
- Frontend: Next.js (React)
- Backend: FastAPI (Python)
- Styling: Tailwind CSS
- AI Model: GPT-4o 