from typing import List
from pydantic import BaseModel, RootModel


class Payload(BaseModel):
    answeredBy: str
    showTitle: str
    seen: str
    externalMessageId: str
    messageGroupId: str


class Button(BaseModel):
    text: str
    payload: str


class Keyboard(BaseModel):
    buttons: List[Button]


class MenuModel(BaseModel):
    id: str
    ts: int
    text: str
    replyToSender: str
    payload: Payload
    keyboard: Keyboard


class ListMenuModel(RootModel[List[MenuModel]]):
    pass
