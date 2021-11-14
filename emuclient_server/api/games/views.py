from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.license_key.decorators import license_key_validator
from api.enums.response_msg import ResponseMessage

import json

from .serializers import GameSerializer, CatalogueSerializer

from .models import Catalogue, Game
from .scraping import GameScraping

@csrf_exempt
@api_view(['POST'])
@license_key_validator
def create_game_catalogue(request):
    body = json.loads(request.body)

    try:
        catalogue = Catalogue.objects.create(platform=body.get('platform'))

        gamelist = GameScraping.retrieve_gameslist_from_page(body.get('url'))[0:15]        
 
        for game in gamelist:
            Game.objects.create(
                game_id   = game.get('id'),
                title     = game.get('title'),
                catalogue = catalogue
            )

        return Response({
            "status": True,
            "message": "Game catalogue created!"
        }, status=200)

    except Exception as e:
        return Response({
            "status": False,
            "reason": f"{ResponseMessage.UNEXPECTED_ERROR.value}: {str(e)}" 
        }, status=500)


@csrf_exempt
@api_view(['GET'])
@license_key_validator
def list_games(request):    
    try:
        games = Game.objects.all()        
        
        return Response({
            "status": True,
            "data": GameSerializer(games) 
        })

    except Exception as e:
        return Response({
            "status": False,
            "message": f"{ResponseMessage.UNEXPECTED_ERROR.value}: {str(e)}"
        })

@csrf_exempt
@api_view(['GET'])
@license_key_validator
def filter_games_by_catalogue(request):
    try:
        catalogue = Catalogue.objects.get(platform=request.GET.get('catalogue'))
    
        games = Game.objects.filter(catalogue=catalogue)

        return Response({
            "status": True,
            "data": GameSerializer(games)
        })

    except Exception as e:
        return Response({
            "status": False,
            "message": f"{ResponseMessage.UNEXPECTED_ERROR.value}: {str(e)}"
        })

@csrf_exempt
@api_view(['GET'])
@license_key_validator
def list_games_catalogue(request):    
    try:
        catalogues = Catalogue.objects.all()        

        return Response({
            "status": True,
            "data": CatalogueSerializer(catalogues) 
        })

    except Exception as e:
        return Response({
            "status": False,
            "message": f"{ResponseMessage.UNEXPECTED_ERROR.value}: {str(e)}"
        })
