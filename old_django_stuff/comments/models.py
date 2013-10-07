from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime

class Comment(models.Model):
    """
    Model class for user comment
    """

    #TODO: ForeignKey Author
    content = models.TextField()
    pub_date = models.DateTimeField()
    #comment_status = models.IntegerField()

    # Generic Foreign Key to other models
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    def __unicode__(self):
        return self.content
    