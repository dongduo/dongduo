from django.db import models

class UserProfile(models.Model):
    """
    The User Profile
    """

    #TODO: VoteApp
    #TODO: figure out boundary between profile and auth
    nickname = models.CharField(max_length=10)
    birthday = models.DateField()  

    def __unicode__(self):
        return "<%s, %s>" % (self.nickname, self.birthday)
    
