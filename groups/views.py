from models import Group, Pitch, Proposal, Vote, Comment, Citation, CitationRequired
from rest_framework import generics, status
from rest_framework.response import Response
from serializers import UserSerializer, GroupSerializer, PitchSerializer, ProposalSerializer, VoteSerializer, CommentSerializer, CitationSerializer, CitationRequiredSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from forms import PitchForm
from django.core.context_processors import csrf
from django.shortcuts import render, redirect


class CreateUser(APIView):
    """
    Create user...
    """
    def post(self, request):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.DATA["username"])
            token = Token.objects.create(user=user)
            headers = {"Authorization": "Token " + token.key}
            return Response(headers=headers, status=status.HTTP_201_CREATED)
        else:
            # we should be doing something here like returning
            # a bad status code. The examples show how to do this.
            # Stop being lazy.
            pass


class GroupList(generics.ListCreateAPIView):
    """
    List all groups, or create a new group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, and destroy group objects.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.accepted_renderer.format == 'html':
            return Response({'group':self.object}, template_name='group_detail.html')
        serializer = GroupSerializer(self.object)
        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and destroy user object.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.accepted_renderer.format == 'html':
            user = self.object
            groups = Group.objects.filter(members__id=user.id)
            return Response({'user':self.object,
                             'groups':groups},
                            template_name='user_detail.html')
        else:
            serializer = UserSerializer(self.object)
            return Response(serializer.data)

class PitchCreate(generics.CreateAPIView):
    """
    create a pitch.
    """
    serializer_class = PitchSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = PitchForm()
            c = {'form': form}
            c.update(csrf(request))
            return render(request, 'pitch_create.html', c)
        else:
            # this request is bad. we should tell them so.
            # This code just errors out
            pass

    def post(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = PitchForm(request.POST)
            if form.is_valid():
                pitch = form.save(commit=False)
                pitch.creator = request.user
                pitch.group_id = kwargs["group_pk"]
                pitch.save()
                return redirect('/groups/' + str(kwargs["group_pk"]))

class PitchDetail(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PitchSerializer(Pitch.objects.get(pk=kwargs['pk']))
        serializer.data.update({'fuck please work': 'goddamnit'})
        return Response(serializer.data)

class PitchView(APIView):
    def get(self, request, format=None):
        pass


class PitchList(generics.ListCreateAPIView):
    """
    List all pitches, or create a new pitch.
    """
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer


class ProposalList(generics.ListCreateAPIView):
    """
    List all proposals, or create a new proposal.
    """
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class VoteList(generics.ListCreateAPIView):
    """
    List all votes, or create a new vote.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all votes, or create a new vote.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CitationList(generics.ListCreateAPIView):
    """
    List all citations, or create a new citation.
    """
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer


class CitationRequiredList(generics.ListCreateAPIView):
    """
    List all citation required flags, or create a new one.
    """
    queryset = CitationRequired.objects.all()
    serializer_class = CitationRequiredSerializer