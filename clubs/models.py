from django.db import models

# Create your models here.

class Clubs(models.Model):
    name = models.CharField(max_length = 100)
    foundation = models.PositiveIntegerField()
    championship = models.PositiveIntegerField()
    history = models.TextField(blank = True, null = True)
    founders = models.CharField(max_length = 300)
    followers = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name   


