from django.db import models
from authentication.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Education(models.Model):
    class Level(models.TextChoices):
        BAC="Bac"
        LICENCE_1="Bac +1"
        LICENCE_2="Bac +2"
        LICENCE_3="Bac +3"
        MASTER_1="Bac +4"
        MASTER2_2="Bac +5"
        PhD="Doctorat"

    title=models.CharField(max_length=100)
    year=models.IntegerField(
                             validators=[MinValueValidator(1900),MinValueValidator(2023)])
    level = models.CharField(choices=Level.choices,max_length=10)
    user_id=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
