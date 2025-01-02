import os
import json
import httpx
from typing import Any, Optional

from anthropic import Anthropic


class RecordingClient(httpx.Client):
    def __init__(
        self,
        save_dir: str = "recordings",
        request_counter: int = 0,
        *args: Any,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.save_dir = save_dir
        self.request_counter = request_counter
        os.makedirs(self.save_dir, exist_ok=True)

    def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        # Save request details
        current_count = self.request_counter
        self.request_counter += 1

        # Save request headers
        headers = kwargs.get("headers", {})
        request_headers_file = os.path.join(
            self.save_dir, f"{current_count}_request_headers.json"
        )
        with open(request_headers_file, "w") as f:
            json.dump(dict(headers), f, indent=2)

        # Save request body if it exists
        body = kwargs.get("content") or kwargs.get("data")
        if body:
            request_body_file = os.path.join(
                self.save_dir, f"{current_count}_request_body.json"
            )
            if isinstance(body, (str, bytes)):
                mode = "wb" if isinstance(body, bytes) else "w"
                with open(request_body_file, mode) as f:
                    f.write(body)
            else:
                with open(request_body_file, "w") as f:
                    json.dump(body, f, indent=2)

        # Make the actual request
        response = super().request(method, url, **kwargs)

        # Save response body
        response_data = response.content
        response_body_file = os.path.join(
            self.save_dir, f"{current_count}_response_body.json"
        )
        with open(response_body_file, "wb") as f:
            f.write(response_data)

        # Save response headers
        response_headers = {
            "Status-Code": response.status_code,
            **dict(response.headers),
        }
        response_headers_file = os.path.join(
            self.save_dir, f"{current_count}_response_headers.json"
        )
        with open(response_headers_file, "w") as f:
            json.dump(response_headers, f, indent=2)

        return response


if __name__ == "__main__":
    MODEL = "claude-3-haiku-20240307"

    http_client = RecordingClient()

    # Get the original base URL from Anthropic
    client = Anthropic(http_client=http_client)

    # Make some API calls
    for i in range(3):
        print(f"\nCall {i + 1}:")

        message = client.messages.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": f"Give me a one-sentence story about a cat (response #{i + 1})",
                }
            ],
            max_tokens=128,
            temperature=0.7,
            stream=False,
        )

        print(f"Content: {message.content}")
        print(f"Model: {message.model}")
        print(f"Finish reason: {message.stop_reason}")
