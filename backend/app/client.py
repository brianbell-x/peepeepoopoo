import os
import base64
import logging
from openai import AsyncOpenAI # Use AsyncOpenAI for FastAPI compatibility

# Configure logging
logger = logging.getLogger(__name__)

# Initialize OpenAI client
# It's best practice to load the API key from environment variables
# Ensure OPENAI_API_KEY is set in your environment
try:
    client = AsyncOpenAI()
    # You can add api_key=os.environ.get("OPENAI_API_KEY") if needed,
    # but the library often picks it up automatically if the env var is set.
    logger.info("OpenAI client initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    client = None # Set client to None if initialization fails

async def call_gpt4o_vision_api(car_bytes: bytes, part_bytes: bytes) -> bytes | None:
    """
    Calls the GPT-4o Vision API to generate the modified car image.

    Args:
        car_bytes: Bytes of the user's car image.
        part_bytes: Bytes of the modification part image.

    Returns:
        Bytes of the generated image, or None if an error occurs.
    """
    if not client:
        logger.error("OpenAI client is not initialized. Cannot make API call.")
        return None

    logger.info("Preparing request for GPT-4o Vision API...")

    # Encode images to base64
    base64_car_image = base64.b64encode(car_bytes).decode('utf-8')
    base64_part_image = base64.b64encode(part_bytes).decode('utf-8')

    # Construct the prompt (adjust as needed for optimal results)
    prompt_text = (
        "You are an expert automotive visualizer. "
        "Take the first image (the car) and realistically apply the modification shown in the second image (the part) onto the car. "
        "Ensure the perspective, lighting, and scale are consistent. "
        "Return only the final modified image of the car, preferably with a clean or transparent background."
    )

    try:
        logger.info("Sending request to OpenAI API...")
        response = await client.chat.completions.create(
            model="gpt-4o", # Use the appropriate GPT-4o model ID
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_car_image}" # Assuming JPEG, adjust if needed
                            },
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_part_image}" # Assuming PNG, adjust if needed
                            },
                        },
                    ],
                }
            ],
            max_tokens=1000 # Adjust max_tokens if needed
        )
        logger.info("Received response from OpenAI API.")

        # --- Placeholder for extracting the generated image from the response ---
        # The actual response structure might vary. You'll need to inspect the
        # response object (response.choices[0].message.content or similar)
        # to find how the image is returned (e.g., as a URL, base64 string, etc.)
        # and then decode/download it.

        # For now, let's simulate returning the original car image bytes
        # Replace this with actual image extraction logic
        logger.warning("Placeholder: Image extraction from GPT-4o response not implemented. Returning original car image.")
        return car_bytes # Placeholder return

    except Exception as e:
        logger.error(f"Error calling OpenAI API: {e}")
        return None
