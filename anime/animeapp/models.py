from django.db import models

# Create your models here.
class Anime(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    seasons=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name