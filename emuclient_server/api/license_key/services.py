from uuid import uuid4

from .models import LicenseKey

class LicenseKeyService:
    
    @staticmethod
    def createKey() -> str:
        key = str(uuid4())

        LicenseKey.objects.create(
            key = key
        )

        return key

    
    @staticmethod
    def validate(license_key: str) -> bool:
        return LicenseKey.objects.get(key=license_key) is not None

