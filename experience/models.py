from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Experienc(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    post=models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1900),MinValueValidator(2023)])
    user_id=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
