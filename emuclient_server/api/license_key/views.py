from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.enums.response_msg import ResponseMessage

from .services import LicenseKeyService

@csrf_exempt
@api_view(["POST"])
def generate_license_key(request):        
    license_key = LicenseKeyService.createKey()
    return Response({
        "status": True,
        "licenseKey": license_key
    } if license_key is None else {
        "status": False,
        "reason": ResponseMessage.UNEXPECTED_ERROR
    })
