from django.db import models
from django.contrib.contenttypes import generic
from comments.models import Comment

class Question(models.Model):
    """
    Model for a question in zhidao
    """

    #TODO: Author
    #TODO: VoteApp

    pub_date = models.DateTimeField()
    title    = models.CharField(max_length=200)
    detail   = models.TextField()

    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)

    #status   = models.IntegerField()


class Answer(models.Model):
    """
    Model for an answer in zhidao
    """

    #TODO: Author
    #TODO: VoteApp

    pub_date  = models.DateTimeField()
    detail    = models.TextField()
    question  = models.ForeignKey(Question)

    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)

    #status = models.IntegerField()
