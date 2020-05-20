from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect



class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    likes       = models.ManyToManyField(User,related_name='likes',blank=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cont = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title,str(self.user.username)   )

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

    def approve(self):
        self.approved_comment = True
        self.save()
