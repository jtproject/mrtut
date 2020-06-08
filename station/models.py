# Imports
'''3rd Party'''

'''Django official'''
from django.conf import settings
from django.db import models
'''Project related'''
from essays.models import Essay


# Global variables
_U = settings.AUTH_USER_MODEL


# Model classes
''' Station members '''
class StationMembersList(models.Model):
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)


''' Station contributors '''
class StationContribsList(models.Model):
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)


''' Station essays '''
class StationEssaysList(models.Model):
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    essay = models.ForeignKey(Essay, on_delete=models.CASCADE)
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


''' Station model '''
class Station(models.Model):
    founder = models.ForeignKey(_U, related_name='stationfounder', null=True, on_delete=models.SET_NULL)
    founded_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    members = models.ForeignKey(_U, related_name='stationmembers', null=True, blank=True, on_delete=models.CASCADE)
    contribs = models.ManyToManyField(_U, related_name='stationcontribs', blank=True, through=StationContribsList)
    essays = models.ManyToManyField(Essay, related_name='stationessays', blank=True, through=StationEssaysList)
    #verses = models.ManyToManyField('Essay', related_name='stationcontribs', blank=True, through=StationContribs)




'''
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #image = models.FileField(upload_to='images/', blank=True, null=True)
    up = models.ManyToManyField(_U, related_name='upuser', blank=True, through=EssayVoteUp)
    down = models.ManyToManyField(_U, related_name='downuser', blank=True, through=EssayVoteDown)

    class Meta:
        ordering = ['-id']

    @property
    def is_share(self):
        return self.parent != None

    def concat_content(self):
        cc = str(self.content)[0:ADMIN_MAX_CONTENT_STRING_LENGTH]
        if len(cc) == ADMIN_MAX_CONTENT_STRING_LENGTH:
            cc += '...'
        return cc
'''
