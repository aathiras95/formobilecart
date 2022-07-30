from django.db import models


# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=80)
    password=models.CharField(max_length=80)

class MobileProducts(models.Model):
    pro_cat=models.CharField(max_length=100)
    pro_code=models.CharField(max_length=100,primary_key=True)
    pro_name=models.CharField(max_length=80)
    pro_ram = models.CharField(max_length=80)
    pro_dis=models.CharField(max_length=90)
    pro_camera = models.CharField(max_length=80)
    pro_battery = models.CharField(max_length=80)
    pro_price=models.PositiveIntegerField()
    pro_offprice=models.PositiveIntegerField(null=True)
    pro_processor=models.CharField(max_length=150)
    pro_warrenty=models.CharField(max_length=150)
    pro_specification=models.CharField(max_length=150)
    pro_img=models.ImageField(upload_to='mobileimages',null=True)


