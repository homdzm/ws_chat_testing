import pytest
import httpx
from dotenv import load_dotenv
import os

from src.utils import create_user_data
from src.models.user_form_models import UserFormModel

load_dotenv()
BASE_API_URL = os.getenv("BASE_API_URL")
BASE_WS_URL = os.getenv("BASE_WS_URL")


@pytest.mark.positive
@pytest.mark.asyncio
async def test_send_valid_form(session_id):
    url = f"{BASE_API_URL}/users"
    payload = create_user_data(session_id)
    headers = {
        "Content-Type": "application/json",
        "session-id": session_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    response.raise_for_status()  # Поймает любые ошибки HTTP
    user = UserFormModel(**response.json())

    assert response.status_code == 200
    assert user.id == session_id
    assert user.email == payload["email"]
    assert user.fullName == payload["fullName"]

@pytest.mark.negative
@pytest.mark.asyncio
async def test_send_invalid_form(session_id):
    url = f"{BASE_API_URL}/users"
    payload = create_user_data(session_id)
    headers = {
        "Content-Type": "application/json",
        "session-id": session_id
    }
    payload["email"] = "invalid_email@"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    assert response.status_code == 400, f"Expected status code 400, but received {response.status_code}"
    assert "Invalid email format" in response.json()
