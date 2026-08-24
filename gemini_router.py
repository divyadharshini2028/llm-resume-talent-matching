import os
import time
from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# LOAD API KEYS
# ============================================================

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

# Remove empty values
API_KEYS = [key.strip() for key in API_KEYS if key and key.strip()]


if not API_KEYS:
    raise ValueError(
        "No Gemini API keys found. "
        "Please add GEMINI_API_KEY_1, GEMINI_API_KEY_2, "
        "and/or GEMINI_API_KEY_3 to your .env file."
    )


# ============================================================
# CREATE GEMINI CLIENTS
# ============================================================

clients = []

for key in API_KEYS:
    clients.append(
        genai.Client(api_key=key)
    )


# ============================================================
# ROUTER
# ============================================================

class GeminiRouter:

    def __init__(self, clients):
        self.clients = clients
        self.current_key = 0

    # --------------------------------------------------------
    # Generate content
    # --------------------------------------------------------

    def generate_content(self, model, contents, **kwargs):

        total_keys = len(self.clients)

        # Try every available API key
        for attempt in range(total_keys):

            key_index = (self.current_key + attempt) % total_keys

            client = self.clients[key_index]

            print(
                f"\n[Gemini Router] Trying API key "
                f"{key_index + 1}/{total_keys}"
            )

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=contents,
                    **kwargs
                )

                # ------------------------------------------------
                # SUCCESS
                # ------------------------------------------------

                self.current_key = key_index

                print(
                    f"[Gemini Router] API key "
                    f"{key_index + 1} succeeded."
                )

                return response

            except Exception as error:

                error_text = str(error).lower()

                print(
                    f"[Gemini Router] API key "
                    f"{key_index + 1} failed."
                )

                print(
                    f"[Gemini Router] Error: {error}"
                )

                # ------------------------------------------------
                # QUOTA / RATE LIMIT
                # ------------------------------------------------

                quota_error = (
                    "429" in error_text
                    or "resource_exhausted" in error_text
                    or "quota" in error_text
                    or "rate limit" in error_text
                    or "too many requests" in error_text
                )

                # ------------------------------------------------
                # TEMPORARY SERVER ERROR
                # ------------------------------------------------

                server_error = (
                    "503" in error_text
                    or "unavailable" in error_text
                    or "service unavailable" in error_text
                )

                if quota_error or server_error:

                    if key_index + 1 < total_keys:

                        print(
                            f"[Gemini Router] Switching from "
                            f"API key {key_index + 1} "
                            f"to API key {key_index + 2}..."
                        )

                        # Small delay before switching
                        time.sleep(1)

                        continue

                # ------------------------------------------------
                # OTHER ERROR
                # ------------------------------------------------

                # If this is not a quota/server error,
                # don't silently hide it.
                raise error

        # ========================================================
        # ALL KEYS FAILED
        # ========================================================

        raise RuntimeError(
            "All Gemini API keys failed. "
            "Please check your API keys, quota, model name, "
            "and Gemini API availability."
        )


# ============================================================
# CREATE GLOBAL ROUTER INSTANCE
# ============================================================

gemini_router = GeminiRouter(clients)