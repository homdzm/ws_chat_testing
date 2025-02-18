import pytest
import pytest_asyncio
import httpx
import websockets
import time
import uuid
import os
from dotenv import load_dotenv


load_dotenv()
BASE_API_URL = os.getenv("BASE_API_URL")
BASE_WS_URL = os.getenv("BASE_WS_URL")


@pytest_asyncio.fixture
async def session_id():
    url = f"{BASE_API_URL}/users?ts={int(time.time() * 1000)}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            session_data = response.json()
            return session_data.get("id")
        except httpx.RequestError as e:
            pytest.fail(f"Request session_id failed: {e}")

@pytest_asyncio.fixture
async def ws_client(session_id):
    try:
        ws_url = f"{BASE_WS_URL}/ws/{uuid.uuid4()}?session-id={session_id}"
        async with websockets.connect(ws_url) as websocket:
            await websocket.ping()
            print("Successfully connected to WebSocket, server responded to ping!")
            yield websocket, session_id
            await websocket.close()
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Websockets connection error: {e}")

@pytest.fixture
def menu_buttons():
    return ["Стоимость системы", "Запланировать демо", "Продукты", "Решения",
            "Варианты установки", "Шаблон ТЗ", "Документация", "Описание API",
            "Стать партнером"]