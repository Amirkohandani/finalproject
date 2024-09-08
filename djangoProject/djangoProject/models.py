from django.db import models
class VehicleData(models.Model):
    url = models.TextField()
    title = models.TextField()
    time = models.TextField()
    year = models.TextField()
    image = models.TextField()
    mileage = models.TextField()
    location = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.TextField()
    class Meta:
        db_table = 'vehicle_data'
        app_label = 'vehicle_data'