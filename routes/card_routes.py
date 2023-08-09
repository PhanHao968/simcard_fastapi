from fastapi import APIRouter,status
from config.database import collection_name
from models.card_model import Card
from schemas.card_schemas import card_serializer,cards_serializer
from bson import ObjectId

card_api_router = APIRouter()

@card_api_router.get("/")
async def get_card():
    cards = cards_serializer(collection_name.find())
    return {"status":"ok","data":cards}

@card_api_router.get("/{id}")
async def get_card(id: str):
    card = cards_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status":"ok","data":card}

@card_api_router.post("/")
async def post_card(card: Card):
    _id = collection_name.insert_one(dict(card))
    card = cards_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": card}

@card_api_router.put("/{id}")
async def update_card(id: str, card: Card):
    collection_name.find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(card)
    })
    card = cards_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": card}

@card_api_router.delete("/{id}")
async def delete_card(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

