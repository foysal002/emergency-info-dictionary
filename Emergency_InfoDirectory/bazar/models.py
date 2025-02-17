from django.db import models

# Create your models here.
class Bazar(models.Model):
    bazar_id = models.IntegerField(primary_key=True, db_column='ID')
    bazar_name = models.CharField(max_length=50,db_column='Name')
    contact_no = models.IntegerField(db_column='Contact No')
    address = models.CharField(max_length=50,db_column='Address')
    subdistrict = models.CharField(max_length=50,db_column='Subdistrict')
    district = models.CharField(max_length=50,db_column='District')
    division = models.CharField(max_length=50,db_column='Division')