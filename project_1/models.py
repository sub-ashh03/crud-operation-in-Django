from django.db import models

class Product(models.Model):

    product_name=models.CharField(max_length=100,null=True)
    product_code=models.CharField(max_length=100,null=True)
    price=models.FloatField(default=0)
    gst=models.IntegerField(default=0)

class studentData(models.Model):
    name=models.CharField(max_length=30)
    mail=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=30)

    def __str__(self) :
        return self.name
