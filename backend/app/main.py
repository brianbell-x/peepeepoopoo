import io
import logging
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware # Import CORS middleware

from .client import call_gpt4o_vision_api # Import the client function

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ModStudio.ai Backend", version="0.1.0")

# --- Add CORS Middleware ---
# This is crucial for allowing the frontend (running on a different port/domain)
# to communicate with the backend.
# Adjust origins as needed for production.
origins = [
    "http://localhost:3000", # Default Next.js dev server
    "http://127.0.0.1:3000",
    # Add your deployed frontend URL here if applicable
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
async def read_root():
    """ Basic health check endpoint. """
    return {"message": "ModStudio.ai Backend is running"}

@app.post("/generate")
async def generate_modification(
    car_image: UploadFile = File(..., description="User's car image"),
    part_image: UploadFile = File(..., description="Modification part image")
):
    """
    Accepts car and part images, processes them (placeholder),
    and returns the generated image.
    """
    logger.info(f"Received request to generate modification.")
    logger.info(f"Car image: {car_image.filename}, content type: {car_image.content_type}")
    logger.info(f"Part image: {part_image.filename}, content type: {part_image.content_type}")

    # Define allowed content types
    allowed_content_types = ["image/jpeg", "image/png", "image/webp"]
    if car_image.content_type not in allowed_content_types or part_image.content_type not in allowed_content_types:
        logger.warning("Invalid file type uploaded.")
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload JPG, PNG, or WebP images.")

    try:
        # 1. Read image bytes
        logger.info("Reading image bytes...")
        car_bytes = await car_image.read()
        part_bytes = await part_image.read()
        logger.info("Image bytes read successfully.")

        # 2. Call the client function
        logger.info("Calling GPT-4o Vision API client function...")
        generated_image_bytes = await call_gpt4o_vision_api(car_bytes, part_bytes)

        if generated_image_bytes:
            logger.info("Received generated image bytes from client.")
            # Determine media type (placeholder - ideally, the API tells us or we detect it)
            # For now, assume the output is the same type as the input car image, or default to PNG
            media_type = car_image.content_type or "image/png"
            return StreamingResponse(io.BytesIO(generated_image_bytes), media_type=media_type)
        else:
            logger.error("GPT-4o client function returned None.")
            raise HTTPException(status_code=500, detail="Failed to generate image using AI model")

    except HTTPException as http_exc:
        # Re-raise HTTPExceptions directly
        raise http_exc
    except Exception as e:
        logger.error(f"An unexpected error occurred during generation: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
    finally:
        # Ensure files are closed even if errors occur
        try:
            await car_image.close()
            await part_image.close()
        except Exception as close_exc:
            logger.error(f"Error closing file handles: {close_exc}")
