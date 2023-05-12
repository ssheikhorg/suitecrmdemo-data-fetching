from hashlib import md5

from httpx import AsyncClient, Timeout, get

import json

# url = "https://suitecrmdemo.dtbc.eu/index.php?"
url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"


def httpx_timeout(timeout: float = 90.0, connect: float = 90.0) -> Timeout:
    return Timeout(timeout=timeout, connect=connect)


async def get_session_id() -> dict:
    payload = {
        "method": "login",
        "input_type": "JSON",
        "response_type": "JSON",
        "rest_data": {
            "user_auth": {
                "user_name": "Demo",
                "password": md5("demo".encode()).hexdigest(),
                "version": "1"
            },
            "application_name": "RestTest"
        }
    }
    try:
        async with AsyncClient() as client:
            response = await client.get(url, params=payload)
            response = json.loads(response.text)
            return response
    except Exception as e:
        print(f"Error: {e}")
        return str(e)
