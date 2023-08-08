def card_serializer(card) -> dict:
    return {
        "id":str(card["_id"]),
        "network": card["network"],
        "phone_number": card["phone_number"],
        "price": card["price"],
        "category": card["category"],
        "detail": card["detail"],
        "date": card["date"]
    }

def cards_serializer(cards) -> list:
    return [card_serializer(card) for card in cards]