# Imports
'''3rd Party'''

'''Django official'''
from django.conf import settings
from django.db import models
'''Project related'''
from jsys.globals import GlobalVariables


# Global variables
_U = settings.AUTH_USER_MODEL
ADMIN_MAX_CONTENT_STRING_LENGTH = GlobalVariables.ADMIN_MAX_CONTENT_STRING_LENGTH


# Model classes
''' Vote logs for essays '''
class EssayVoteUp(models.Model):
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    post = models.ForeignKey('Essay', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
class EssayVoteDown(models.Model):
    user = models.ForeignKey(_U, on_delete=models.CASCADE)
    post = models.ForeignKey('Essay', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

''' Essay model '''
class Essay(models.Model):
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

class Post(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    up = models.ManyToManyField(User, related_name='upuser', blank=True, through=PostUp)
    down = models.ManyToManyField(User, related_name='downuser', blank=True, through=PostDown)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_share:
            return f'[POST{self.id}] :: < SHARE_POST{self.parent.id} >'
        else:
            content_shortened = str(self.content)[0:30]
            if len(content_shortened) == 30:
                content_shortened += '...'
            return f'[POST{self.id}] :: {content_shortened}'
'''
