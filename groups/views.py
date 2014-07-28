from models import (
    Group, Pitch, Proposal, Vote, Comment, Citation, CitationRequired
)
from rest_framework import generics, status
from rest_framework.response import Response
from serializers import (
    UserSerializer, GroupSerializer, PitchSerializer, ProposalSerializer,
    VoteSerializer, CommentSerializer, CitationSerializer,
    CitationRequiredSerializer
)
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.renderers import (TemplateHTMLRenderer,
    JSONRenderer, BrowsableAPIRenderer
)
from forms import PitchForm, CommentForm, GroupForm, ProposalForm
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
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = GroupSerializer(self.object)
        if self.request.accepted_renderer.format == 'html':
            return Response({'group': serializer.data},
                            template_name='group_detail.html')
        return Response(serializer.data)


class ProposalDetail(generics.RetrieveAPIView):
    queryset = Proposal.objects.all()

    serializer_class = ProposalSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        serializer = Proposal(Pitch.objects.get(pk=kwargs['pk']))
        if self.request.accepted_renderer.format == 'html':
            # we have to set unpack the tree structure here for the template
            serializer.data['comments'] = RenderTree(
                serializer.data['comments'])
            return Response({'proposal': serializer.data},
                            template_name='proposal_detail.html')

        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and destroy user object.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.accepted_renderer.format == 'html':
            user = self.object
            groups = Group.objects.filter(members__id=user.id)
            return Response({'user': self.object,
                             'groups': groups},
                            template_name='user_detail.html')
        else:
            serializer = UserSerializer(self.object)
            return Response(serializer.data)


class CommentCreate(generics.CreateAPIView):
    """
    create a reply comment..
    """
    serializer_class = CommentSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = CommentForm()
            c = {'form': form}
            c.update(csrf(request))
            return render(request, 'comment_create.html', c)

    def post(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = CommentForm(request.POST)
            if form.is_valid():
                if kwargs.get('pk', '') != '':
                    parent = Comment.objects.get(pk=kwargs['pk'])
                else:
                    parent = Pitch.objects.get(pk=kwargs['pitch_pk'])\
                        .comments.all()[0]
                parent.add_child(text=form.cleaned_data['text'],
                                 creator=request.user)
                return redirect('/groups/' + str(kwargs["group_pk"]) +
                                "/pitch/" + str(kwargs['pitch_pk']))


class GroupCreate(generics.CreateAPIView):
    """
    Create a group!
    """
    serializer_class = PitchSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = GroupForm()
            c = {'form':form}
            c.update(csrf(request))
            return render(request, 'group_create.html', c)

    def post(self, request, *args, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = GroupForm(request.POST)
            if form.is_valid():
                group = form.save(commit=False)
                group.creator = request.user
                group.save()
                group.members.add(request.user)
                group.save()
                return redirect('/groups/' + str(group.id))


class ProposalCreate(generics.CreateAPIView):
    """
    Create a proposal
    """
    serializer_class = ProposalSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = ProposalForm()
            c = {'form': form}
            c.update(csrf(request))
            return render(request, 'proposal_create.html', c)

    def post(self, request, *arg, **kwargs):
        if self.request.accepted_renderer.format == 'html':
            form = ProposalForm(request.POST)
            if form.is_valid():
                pitch = Pitch.objects.get(pk=int(kwargs['pitch_pk']))
                proposal = form.save(commit=False)
                proposal.creator = request.user
                proposal.pitch = pitch
                proposal.save()
                return redirect('/groups/' + str(kwargs["group_pk"]) +
                                "/pitch/" + str(kwargs['pitch_pk']))

class PitchCreate(generics.CreateAPIView):
    """
    create a pitch.
    """
    serializer_class = PitchSerializer
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

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
                Comment.add_root(creator=User.objects.all()[0],
                                 content_object=pitch, text='')
                return redirect('/groups/' + str(kwargs["group_pk"]))

class PitchDetail(APIView):
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,
                        BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        serializer = PitchSerializer(Pitch.objects.get(pk=kwargs['pk']))
        if self.request.accepted_renderer.format == 'html':
            # we have to set unpack the tree structure here for the template
            serializer.data['comments'] = RenderTree(
                serializer.data['comments']
            )
            return Response({'pitch':serializer.data},
                            template_name='pitch_detail.html')

        return Response(serializer.data)

class PitchView(APIView):
    def get(self, request, format=None):
        pass

def RenderTree(l):
    ret = []
    for i in l:
        if type(i) == list:
            ret = RenderTree(i)
        else:
            ret.append({'ind':'<li>'})
            ret.append(i['data'])
            if 'children' in i.keys():
                ret += RenderTree(i['children'])
            ret.append({'out':'</li>'})
    return ret

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