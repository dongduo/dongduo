from django.db import models
from django.contrib.contenttypes import generic
from comments.models import Comment
from users.models import User

class Post(models.Model):
    """
    Model for a post in blogs
    """

    #TODO: VoteApp
    author   = models.ForeignKey(User)
    pub_date = models.DateTimeField()  
    title    = models.CharField(max_length=200)
    detail   = models.TextField()
   
    
    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)
    
    def __unicode__(self):
        return self.title