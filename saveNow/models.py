from django.db import models
from django.contrib.auth.models import User

class SavePost(models.Model):
    rank = models.CharField(max_length=20)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length = 20)
    email = models.EmailField()
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name