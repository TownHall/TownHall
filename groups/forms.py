__author__ = 'daniel'
from django import forms
from models import Pitch, Comment, Group, Proposal

class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = ['title', 'text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['title', 'text']