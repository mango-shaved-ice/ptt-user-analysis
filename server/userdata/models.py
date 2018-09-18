from django.db import models


class Article(models.Model):
    id = models.CharField(max_length=30, db_index=True, unique=True, primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=256)
    content = models.TextField()
    published = models.DateTimeField()
    ip = models.GenericIPAddressField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    content = models.TextField()
    published = models.DateTimeField()
    ip = models.GenericIPAddressField()
    TAG_TYPES = (('PUSH', 'push'), ('NEUTRAL', 'neutral'), ('BOO', 'boo'))
    tag = models.CharField(max_length=10, choices=TAG_TYPES)
