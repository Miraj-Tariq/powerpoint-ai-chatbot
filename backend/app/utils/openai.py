import traceback
from typing import Optional, Dict, Any

from openai import AzureOpenAI


class OpenAIChatService:
    """
    Encapsulates the interaction with the Azure OpenAI service.
    """

    def __init__(self, endpoint: str, api_key: str, api_version: str, model: str):
        self.endpoint = endpoint
        self.api_key = api_key
        self.api_version = api_version
        self.model = model

    def _get_azure_client(self) -> AzureOpenAI:
        """
        Initialize and return an Azure OpenAI client instance.
        """
        try:
            return AzureOpenAI(
                azure_endpoint=self.endpoint,
                api_key=self.api_key,
                api_version=self.api_version
            )
        except Exception as e:
            raise ConnectionError(f"Failed to initialize Azure OpenAI client: {str(e)}")

    def run_chatGPT(self,
                    gpt_client: AzureOpenAI,
                    system_prompt: str,
                    user_prompt: str,
                    output_schema: Optional[Any] = None) -> Optional[Dict[str, Any]]:
        """
        Executes a ChatGPT completion using the Azure OpenAI client.

        Args:
            gpt_client (AzureOpenAI): An Azure OpenAI client.
            system_prompt (str): System-level instruction to guide the AI.
            user_prompt (str): User-level instruction or query.
            output_schema (Optional[Any]): Optional schema for structured output.

        Returns:
            Optional[Dict[str, Any]]: Parsed response from ChatGPT.
        """
        if not gpt_client:
            gpt_client = self._get_azure_client()

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]

            if output_schema:
                response = gpt_client.beta.chat.completions.parse(
                    model=self.model,
                    messages=messages,
                    response_format=output_schema,
                )
            else:
                response = gpt_client.beta.chat.completions.parse(
                    model=self.model,
                    messages=messages
                )

            return response.choices[0].message.parsed if output_schema else response

        except Exception as e:
            print(
                f"An error occurred:"
                f"\nError Type: {type(e).__name__}"
                f"\nError Message: {str(e)}"
                f"\nTraceback:{traceback.format_exc()}")
            return None
