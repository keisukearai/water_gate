from django.db import models

# Create your models here.
class Area(models.Model):
    area_name = models.CharField(max_length=100)
    area_count = models.IntegerField(default=0)

    def __str__(self):
        return self.area_name