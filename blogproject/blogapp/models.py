from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk}, {self.title}, by {self.user}"