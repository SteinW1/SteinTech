from django.db import models

class Plant(models.Model):
    primary_key = models.AutoField(primary_key=True)
    plant_type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)


class PlantSensorReading(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    time = models.DateTimeField()
    moisture = models.BooleanField()
    sunlight = models.BooleanField()
