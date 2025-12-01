from django.db import models
from user_app.models import User
# Create your models here.

class BlogModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="blog/%y/%m")
    short_description = models.TextField()
    description = models.TextField()