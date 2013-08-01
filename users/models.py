from django.db import models

class User(models.Model):
    """
    Model for a user in users
    """

    #TODO: VoteApp
    #TODO: Other attributes such as Email etc. 
    birthday = models.DateField()  
    name   = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    
