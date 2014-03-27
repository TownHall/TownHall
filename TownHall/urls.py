from django.conf.urls import patterns, include, url

from django.contrib import admin
from groups import views
from TownHall.views import home
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/',
        include(admin.site.urls),
        name='admin'),
    url(r'^groups/$', views.GroupList.as_view(),
        name='list-groups'),
    url(r'^groups/(?P<pk>[0-9]+)/$',
        views.GroupDetail.as_view(),
        name='detail-groups'),
    url(r'^groups/(?P<group_pk>[0-9]+)/pitch/new/$',
        views.PitchCreate.as_view(),
        name='create-pitch'),
    url(r'^proposals/',
        views.ProposalList.as_view(),
        name='list-proposals'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^pitch/(?P<pk>[0-9]+)/$', views.PitchDetail.as_view()),
    url(r'^groups/(?P<group_pk>[0-9]+)/pitch/(?P<pk>[0-9]+)$',
        views.PitchDetail.as_view()),
)
