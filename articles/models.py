from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  
  slug = models.SlugField()

  body = models.TextField()
  
  date = models.DateTimeField(auto_now_add=True)
  thumb = models.ImageField(default='default.png', blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


# add in thumbnail and author later

# python3 manage.py makemigrations
# python3 manage.py migrate

  def __str__(self):
    return self.title
  def snippet(self):
    return self.body[:50]