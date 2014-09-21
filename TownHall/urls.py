# -*- coding: utf-8 -*-
__author__ = 'daniel'

from django.conf.urls import patterns, include, url

from django.contrib import admin
from groups import views
from TownHall.views import home, UserCreate

from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
                       url(r'^$', home.as_view(), name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/',
                           include(admin.site.urls),
                           name='admin'),
                       url(r'^groups/$',
                           views.GroupList.as_view(),
                           name='group-listcreate'
                       ),

                       url(r'^groups/(?P<pk>[0-9]+)/$',
                           views.GroupDetail.as_view(),
                           name='group-retrieveupdatedestroy'
                       ),

                       url(r'^groups/(?P<pk>[0-9]+)/members/$',
                           views.GroupMemberList.as_view(),
                           name='group-memberlist'
                       ),
                       url(r'^groups/(?P<pk>[0-9]+)/join/$',
                           views.JoinGroup.as_view(),
                           name='group-join'
                       ),
                       url(r'^groups/(?P<pk>[0-9]+)/join/$',
                           views.PromoteUser.as_view(),
                           name='group-promote'
                       ),
                       url(r'^groups/(?P<group_pk>[0-9]+)/pitch/new/$',
                           views.PitchCreate.as_view(),
                           name='create-pitch'
                       ),
                       url(r'^proposals/',
                           views.ProposalList.as_view(),
                           name='proposal-list'
                       ),
                       url(r'^users/$',
                           views.UserCreateList.as_view(),
                           name='user-createlist'
                       ),
                       url(r'^users/(?P<pk>[0-9]+)/$',
                           views.UserDetails.as_view(),
                           name='user-retrieveupdatedestroy'
                       ),
                       url(r'users/login/$',
                           views.UserLogin.as_view(),
                           name='user-login'
                       ),
                       url(r'^users/create/$',
                           UserCreate.as_view(),
                           name='user-create'
                       ),
                       url(r'^group/P<pk>[0-9]+)/$')


                       url(r'^pitch/(?P<pk>[0-9]+)/$',
                           views.PitchDetail.as_view(),
                           name='pitch-detail'
                       ),
                       url(r'^groups/(?P<group_pk>[0-9]+)/pitch/'
                           '(?P<pitch_pk>[0-9]+)/comments/(?P<pk>[0-9]+)/reply$',
                           views.CommentCreate.as_view(),
                           name='comment-create-reply'
                          ),
                       url(r'^groups/(?P<group_pk>[0-9]+)/pitch/(?P<pitch_pk>[0-9]+)/'
                           r'comments/new$',
                           views.CommentCreate.as_view(),
                           name='comment-create-new'
                          ),
                       url(r'^groups/create/$',
                           views.GroupCreate.as_view(),
                           name='group-create'
                        ),
                       url(r'^groups/(?P<group_pk>[0-9]+)/pitch/(?P<pitch_pk>[0-9]+)/'
                           r'proposals/new$',
                           views.ProposalCreate.as_view(),
                           name='proposal-create'
                       ),
                       url(r'^groups/(?P<group_pk>[0-9]+)/pitch/(?P<pitch_pk>[0-9]+)/'
                           r'proposals/(?P<pk>[0-9]+)/$',
                           views.ProposalDetail.as_view(),
                           name='proposal-detail'
                          ),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])