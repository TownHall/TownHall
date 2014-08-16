# -*- coding: utf-8 -*-
__author__ = 'daniel'

from rest_framework import serializers
from groups.models import Pitch, Proposal, Comment
import json
from django.core.serializers.json import DjangoJSONEncoder


class ObjectWithCitationRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tagged_object` generic relationship.
    """

    def to_native(self, value):
        """
        Serialize objects with citation.
        """
        if isinstance(value, Pitch):
            return 'Pitch: ' + value.title
        elif isinstance(value, Proposal):
            return 'Proposal: ' + value.title
        if isinstance(value, Comment):
            return 'Comment: ' + value.text

        raise Exception('Unexpected type of tagged object')


class CommentsField(serializers.RelatedField):
    """
    A field to return comment trees
    """

    def to_native(self, value):
        children = value.dump_bulk()
        return json.dumps(children, cls=DjangoJSONEncoder)



