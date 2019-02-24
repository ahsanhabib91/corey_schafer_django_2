from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # CASCADE -> if the User deleted, also delete the Post. But if the Post deleted, do not delete the User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # calculate the canonical/offical/main URL for an object
    def get_absolute_url(self):
        # reverse returns the full path/url as string
        return reverse('post-detail', kwargs={'pk': self.pk})
