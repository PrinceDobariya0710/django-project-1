from django.db import models

# Create your models here.
# class Base(models.Model):
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         managed = False

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=45)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/',default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post {self.title}"