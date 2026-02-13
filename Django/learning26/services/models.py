from django.db import models

class service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    service_price = models.FloatField()
    service_duration = models.IntegerField()
    service_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        db_table = "service"

    def __str__(self):
        return self.service_name