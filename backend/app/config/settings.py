import os
from pathlib import Path

from dotenv import load_dotenv

from app.utils.openai import OpenAIChatService

current_path = Path.cwd()

load_dotenv()


class Settings:
    AOAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AOAI_KEY = os.getenv("AZURE_OPENAI_KEY")
    AOAI_API_VERSION = os.getenv("AZURE_API_VERSION")
    AOAI_MODEL = os.getenv("GPT_MODEL")

    CURRENT_PPT = str(current_path / os.getenv("LOCAL_PPT_FILENAME"))

    GPT_SERVICE = OpenAIChatService(
        f"{AOAI_ENDPOINT}?api-version={AOAI_API_VERSION}",
        AOAI_KEY,
        AOAI_API_VERSION,
        AOAI_MODEL,
    )
    GPT_CLIENT = GPT_SERVICE._get_azure_client()
