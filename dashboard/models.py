from django.db import models

# Create your models here.
class quer(models.Model):
    item_no = models.CharField(max_length=500)
    class Meta:
        db_table = 'quer'