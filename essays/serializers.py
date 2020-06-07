# Imports
'''3rd Party'''
from rest_framework import serializers as _S
'''Django official'''
from django.conf import settings
'''Project related'''
from .models import Essay
from jsys.globals import GlobalVariables


# Global variables
MAX_ESSAY_TITLE_LENGTH = GlobalVariables.MAX_ESSAY_TITLE_LENGTH
MAX_ESSAY_CONTENT_LENGTH = GlobalVariables.MAX_ESSAY_CONTENT_LENGTH
#_U = settings.AUTH_USER_MODEL


# Serializers
'''
    BASIC
'''
class EssaySerializer(_S.Serializer):
    id = _S.IntegerField()
    title = _S.CharField()
    content = _S.CharField()

    class Meta:
        model = Essay
        fields = ['id', 'user', 'title', 'content']


'''
    CREATE NEW ESSAY
'''
class EssayCreateSerializer(_S.Serializer):
    id = _S.IntegerField()
    title = _S.CharField(allow_blank=True, required=False)
    content = _S.CharField(allow_blank=True, required=False)
    user = _S.SerializerMethodField(read_only=True)

    class Meta:
        model = Essay
        fields = ['id', 'user', 'title', 'content']

    def get_user(self, obj):
        return obj.user.username

    def validate_content(self, value):
        if len(value) > MAX_ESSAY_CONTENT_LENGTH:
            raise _S.ValidationError('Your content exceeds the character limit.')
        return value



'''
class PostShareSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(allow_blank=True, required=False)

class PostVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in PAO:
            raise serializers.ValidationError('Can\'t do that.')
        return value

class PostCreateSerializer(serializers.ModelSerializer):
    up = serializers.SerializerMethodField(read_only=True)
    down = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'content', 'up', 'down']
    def get_up(self, obj):
        return obj.up.count()
    def get_down(self, obj):
        return obj.down.count()

    def validate_content(self, value):
        if len(value) > MPL:
            raise serializers.ValidationError('Too long, son!')
        return value

class PostSerializer(serializers.ModelSerializer):
    up = serializers.SerializerMethodField(read_only=True)
    down = serializers.SerializerMethodField(read_only=True)
    parent = PostCreateSerializer(read_only=True)
    vote = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'up', 'down', 'vote', 'is_share', 'parent']
    def get_up(self, obj):
        return obj.up.count()
    def get_down(self, obj):
        return obj.down.count()
    def get_user(self, obj):
        return obj.user.username
    def get_vote(self, obj):
        search_votes_up = PostUp.objects.filter(post=obj.id, user=obj.user)
        search_votes_down = PostDown.objects.filter(post=obj.id, user=obj.user)
        if search_votes_up.exists():
            vote = 'UP'
        elif search_votes_down.exists():
            vote = 'DOWN'
        else:
            vote = ''
        return vote
'''
'''
    def get_content(self, obj):
        content = obj.content
        if obj.is_share:
            content = obj.parent.content
        return content
'''
