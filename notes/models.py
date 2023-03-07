from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Note(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='notes/covers/%Y/%m/%d/')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    is_public = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
