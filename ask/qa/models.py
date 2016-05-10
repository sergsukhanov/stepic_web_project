from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,default=1)
    #likes = models.ManyToManyField(User, related_name='questions', blank=True)
    likes = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=1)
