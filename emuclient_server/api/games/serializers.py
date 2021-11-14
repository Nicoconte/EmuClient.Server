from .models import Catalogue, Game

def GameSerializer(games: list[Game]):
    serialized = []
    for game in games:
        serialized.append({
            "id": game.game_id,
            "title": game.title,
            "catalogue": game.catalogue.platform,
            "created_at": game.created_at
        })    
    
    return serialized


def CatalogueSerializer(catalogues: list[Catalogue]):
    serialized = []

    for cat in catalogues:
        serialized.append({
            "platform": cat.platform
        })

    return serialized