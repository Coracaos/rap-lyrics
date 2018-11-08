from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Rap(models.Model):
    """rap created by the user"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


