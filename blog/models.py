from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50)
    class Meta :
        verbose_name_plural="tag"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    class Meta:
        verbose_name_plural="Post"
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural ="comment"

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
