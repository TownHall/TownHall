__author__ = 'daniel'
from rest_framework import serializers
from models import Group, Pitch, Proposal, Vote, Comment, Citation, CitationRequired
from django.contrib.auth.models import User
from fields import CommentsField
class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the group model.
    """
    class Meta:
        model = Group
        fields = ('creator', 'name', 'description', 'members')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """

    def to_native(self, obj):
        if not self.field_mapping.has_key('comments'):
            self.field_mapping['comments'] = CommentSerializer(required=False, many=True)
        return super(CommentSerializer, self).to_native(obj)

    class Meta:
        model = Comment
        fields = ('creator', 'text')


class PitchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Pitch model.
    """
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Pitch
        fields = ('creator', 'group', 'date_created', 'text', 'title', 'comments')

    def to_native(self, obj):
        ret = super(PitchSerializer, self).to_native(obj)
        print obj.comments.all()
        for i,comment in enumerate(obj.comments.all()):
            ret["comments"][i] = comment.dump_bulk()
        return ret

class ProposalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Proposal model.
    """
    class Meta:
        model = Proposal
        fields = ('creator', 'title', 'text', 'date_created')


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vote model.
    """
    class Meta:
        model = Vote
        fields = ('creator', 'value', 'content_object')


class CitationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Citation model.
    """
    class Meta:
        model = Citation
        fields = ('creator', 'date_created', 'text', 'content_object')


class CitationRequiredSerializer(serializers.ModelSerializer):
    """
    Serializer for the CitationRequired model.
    """
    class Meta:
        model = CitationRequired
        fields = ('creator', 'date_created', 'text', 'content_object')

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
