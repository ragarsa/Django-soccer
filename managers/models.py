from django.db import models

# Create your models here.
class Managers(models.Model):
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    bornplace = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    biography = models.TextField(blank = True, null = True)
    team = models.CharField(max_length = 300)
    championship = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + self.last_name