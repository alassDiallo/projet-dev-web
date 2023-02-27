from django.db import models
from post.models import Post
from authentication.models import User

# Create your models here.

class Comment(models.Model):
    content=models.CharField(max_length=100)
    date=models.DateTimeField()
    post_id=models.ForeignKey(Post,null=False,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,null=False,on_delete=models.CASCADE)
