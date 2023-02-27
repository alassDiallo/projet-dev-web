from django.db import models
from authentication.models import User

# Create your models here.

class Post(models.Model):
    content=models.CharField(max_length=300)
    image=models.ImageField(null=True)
    date=models.DateTimeField()
    nbLike=models.IntegerField(default=0)
    nbDisLike=models.IntegerField(default=0)
    user_id=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
