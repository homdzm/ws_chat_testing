import pytest
import json

from src.utils import create_message
from src.models.menu_models import ListMenuModel

@pytest.mark.asyncio
@pytest.mark.positive
async def test_check_menu_response(ws_client, menu_buttons):
    websocket, session_id  = ws_client
    msg_menu = create_message(session_id, "Меню")

    await websocket.send(json.dumps(msg_menu))
    response = await websocket.recv()

    menu = ListMenuModel.model_validate_json(response)
    assert menu.root[0].payload.externalMessageId == msg_menu["id"]

    menu_buttons_form_response = [button.text for button in menu.root[0].keyboard.buttons]
    assert sorted(menu_buttons_form_response) == sorted(menu_buttons)


