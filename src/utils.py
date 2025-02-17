import time
import uuid
from faker import Faker


fake = Faker("ru_RU")

def create_message(session_id: str, text: str, ):
    return {
        "id": str(uuid.uuid4()),
        "ts": int(time.time() * 1000),
        "sessionId": session_id,
        "text": text,
        "sender": session_id
            }

def create_user_data(session_id: str):
    return {
        "id": session_id,
        "login": session_id,
        "email": fake.email(),
        "fullName": fake.last_name() + " " + fake.first_name(),
        "payload": {}
            }