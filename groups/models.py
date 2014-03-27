from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from treebeard.mp_tree import MP_Node


class Group(models.Model):
    creator = models.ForeignKey(User, related_name='creator')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User)

    def __string__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Vote(models.Model):
    creator = models.ForeignKey(User)
    value = models.SmallIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Citation(models.Model):
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Comment(MP_Node):
    creator = models.ForeignKey(User)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    votes = GenericRelation(Vote)
    
    def __unicode__(self):
        return self.text


class Pitch(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    group = models.ForeignKey(Group)
    date_created = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation(Vote)
    comments = GenericRelation(Comment)
    cites = GenericRelation(Citation)

class Proposal(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation(Vote)
    comments = GenericRelation(Comment)


class CitationRequired(models.Model):
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
