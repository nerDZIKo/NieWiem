from django.db import models

# Create your models here.
class FireLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    hour = models.FloatField()

    @classmethod
    def createFire(cls, value_0, value_1, value_2):
        new_object = cls(latitude = value_0, longitude = value_1, hour = value_2)
        new_object.save()
        return new_object