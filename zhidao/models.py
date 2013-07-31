from django.db import models
from django.contrib.contenttypes import generic
from comments.models import Comment
from users.models import User

class Question(models.Model):
    """
    Model for a question in zhidao
    """

    #TODO: VoteApp
    author   = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title    = models.CharField(max_length=200)
    detail   = models.TextField()

    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)

    #status   = models.IntegerField()
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    """
    Model for an answer in zhidao
    """

    #TODO: VoteApp
    author    = models.ForeignKey(User)
    pub_date  = models.DateTimeField()
    detail    = models.TextField()
    question  = models.ForeignKey(Question)

    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)

    #status = models.IntegerField()
    def __unicode__(self):
        return self.detail
    