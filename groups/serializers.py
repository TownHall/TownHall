__author__ = 'daniel'
from rest_framework import serializers
from models import (
    Group, Pitch, Proposal, Vote, Comment, Citation, CitationRequired
)
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """
    def to_native(self, obj):
        if not 'comments' in self.field_mapping:
            self.field_mapping['comments'] = CommentSerializer(required=False,
                                                               many=True)
        return super(CommentSerializer, self).to_native(obj)

    class Meta:
        model = Comment
        fields = ('creator', 'text', 'id')


class ProposalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Proposal model.
    """
    comments = CommentSerializer(many=True)

    class Meta:
        model = Proposal
        fields = ('creator', 'title', 'text',
                  'date_created', 'id', 'comments')


class PitchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Pitch model.
    """
    creator = serializers.SlugRelatedField(slug_field='username')
    comments = CommentSerializer(many=True)
    proposal_set = ProposalSerializer(many=True)

    class Meta:
        model = Pitch
        fields = ('creator', 'group', 'date_created', 'text',
                  'title', 'comments', 'id', 'proposal_set')

    def add_users(self, list, users):
        for i in list:
            i['data']['username'] = \
                users.get(pk=i['data']['creator']).username
            i['data']['id'] = i['id']
            if 'children' in i.keys():
                self.add_users(i['children'], users)
    def to_native(self, obj):
        ret = super(PitchSerializer, self).to_native(obj)
        for i,comment in enumerate(obj.comments.all()):
            ret["comments"][i] = Comment.dump_bulk(comment)
            users = User.objects.all()
            self.add_users(ret["comments"][i], users)
        return ret



class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the group model.
    """
    pitch_set = PitchSerializer(many=True, blank=True)

    class Meta:
        model = Group
        fields = ('creator', 'name', 'description', 'members',
                  'pitch_set', 'id')


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
