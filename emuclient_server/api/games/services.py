from .models import Game, Catalogue

class GameService:
    
    @staticmethod
    def create(id: str, title: str, catalogue: Catalogue) -> None:
        Game.objects.create(
            game_id=id,
            title=title,
            catalogue=catalogue
        )
    