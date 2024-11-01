from django.urls import re_path, include
from . import views


urlpatterns = [
    re_path(r'$',views.PostListView.as_view(),name='post_list'),
    re_path(r'^about/$',views.AboutView.as_view(),name='about'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/comment/delete/$', views.deleteComment, name='remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/bdiasa/$', views.add_comment_to_post, name='addcomment'),
    re_path(r'^post/(?P<pk>\d+)/comment/approve/$', views.approveComment, name='approve'),
    re_path(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_remove'),
    ]
