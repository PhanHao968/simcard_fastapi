from typing import List
from fastapi import APIRouter, status, HTTPException, Query
from config.database import collection_name
from models.sim_model import Sim
from schemas.sim_schemas import sims_serializer, sim_serializer
from bson import ObjectId

sim_api_router = APIRouter()

@sim_api_router.get("/")
async def get_sim():
    sims = sims_serializer(collection_name.find())
    return {"status":"Successfully", "data": sims}

@sim_api_router.get("/{id}")
async def get_sim(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sim with id {id} not found")
    sim = sims_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "Successfully", "data": sim}

@sim_api_router.post("/")
async def create_sim(sim: Sim):
    _id = collection_name.insert_one(dict(sim))
    sim = sims_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "Successfully", "data": sim}

@sim_api_router.put("/{id}")
async def update_sim(id: str, sim: Sim):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sim with id {id} not found")
    collection_name.find_one_and_update({"_id": ObjectId(id)},{
        "$set": dict(sim)
    })
    sim = sims_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "Successfully", "data": sim}

@sim_api_router.delete("/{id}")
async def delete_sim(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sim with id {id} not found")
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "Successfully"}

@sim_api_router.get("/search/")
async def search_sim_by_prefix(prefix: str = Query(..., description="Phone number prefix")):
    query = {"phone_number": {"$regex": f"^{prefix}"}}
    result = collection_name.find(query)

    phone_numbers = [sim_serializer(sim) for sim in result]
    return {"matching_phone_numbers": phone_numbers}

@sim_api_router.post("/insert/")
async def create_multiple_sims(sims: List[Sim]):
    created_sims = []
    for sim in sims:
        _id = collection_name.insert_one(dict(sim))
        created_sim = sims_serializer(collection_name.find_one({"_id": _id.inserted_id}))
        created_sims.append(created_sim)

    return {"status": "Successfully", "data": created_sims}
