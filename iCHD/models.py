from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, verbose_name='用户')
    #name = models.CharField('昵称', max_length=32)
    #head_img = models.ImageField('头像', height_field=240, width_field=320, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
