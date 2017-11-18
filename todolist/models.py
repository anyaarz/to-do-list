from django.db import models
from django.utils import timezone



class Article(models.Model):
    class Meta():
        db_table = 'article'

    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
# Create your models here.
