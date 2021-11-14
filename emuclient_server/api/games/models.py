from django.db import models

class Catalogue(models.Model):
    platform = models.CharField(max_length=100)

class Game(models.Model):
    game_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID {self.game_id} - Catalogue {self.catalogue.platform} - Title {self.title} "