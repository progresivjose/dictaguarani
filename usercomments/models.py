from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from words.models import Word

# Create your models here.
class UserComment(models.Model):
    title = models.CharField(max_length=500)
    comment = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, related_name="comment_user_id")
    usercomment = models.ForeignKey('self', related_name="comment_answer_id")
    word = models.ForeignKey(Word, related_name="comment_word_id")

    def __unicode__(self):
        return self.title