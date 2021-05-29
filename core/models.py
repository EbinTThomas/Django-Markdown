from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField(max_length=250)
  thumbnail = models.CharField(max_length=500)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title