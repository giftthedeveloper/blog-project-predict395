from django.db import models
from account.models import Users


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
