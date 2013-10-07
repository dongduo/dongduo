from django.db import models
from users.models import UserProfile
from django.contrib.contenttypes import generic
from comments.models import Comment

class Tweet(models.Model):
    
    #TODO: VoteApp
    author   = models.ForeignKey(UserProfile)
    pub_date = models.DateTimeField()
    detail   = models.TextField(max_length=500)
    fwd_tweet = models.ForeignKey("self", null = True, on_delete = models.SET_NULL)
    
    # Generic Relation to Comment
    comments = generic.GenericRelation(Comment)
    
