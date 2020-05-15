from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#STATUS_CHOICES = (
#   ('draft', 'Draft'),
#   ('published', 'Published'),
#)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField(max_length = 250, null = True, blank = True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    #status = models.CharField(max_length = 10, choices = STATUS_CHOICES,
    #                                                     default ='draft')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
'''
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
'''
