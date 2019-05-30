from django.db import models


class Match(models.Model):
    player1 = models.CharField(max_length=200)
    player2 = models.CharField(max_length=200)
    date_played = models.DateTimeField()
    result = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.player1} vs {self.player2}"
