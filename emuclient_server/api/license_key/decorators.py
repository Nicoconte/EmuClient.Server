from rest_framework.response import Response

from api.license_key.services import LicenseKeyService


from api.enums.response_msg import ResponseMessage

def license_key_validator(f):
    def requestchecker(request, *args):
        key = request.META.get('HTTP_AUTHORIZATION')
        if key == None or not LicenseKeyService.validate(key):
            raise Response({
                "status": False,
                "reason": ResponseMessage.UNAUTHORIZED
            }, status=401)
        return f(request, *args)
    return requestchecker