def sim_serializer(sim) -> dict:
    return {
        "id": str(sim["_id"]),
        "network": sim["network"],
        "phone_number": sim["phone_number"],
        "price": sim["price"],
        "category": sim["category"],
        "detail": sim["detail"],
        "created_at": sim["created_at"],
        "updated_at": sim["updated_at"]
    }

def sims_serializer(sims) -> list:
    return [sim_serializer(sim) for sim in sims]