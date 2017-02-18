from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from accounts.views import UserRegistrationView
from django.contrib.auth.views import login, logout

from blog.views import NewBlogView, HomeView, UpdateBlogView, NewBlogPostView
from blog.views import UpdateBlogPostView, BlogPostDetailView, ShareBlogPostView
from blog.views import SharePostWithBlog, StopSharingPostWithBlog

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', login, {'template_name' : 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

    url(r'^blog/new/$', NewBlogView.as_view(), name='new-blog'),
    url(r'^blog/(?P<pk>\d+)/update/$', UpdateBlogView.as_view(), name='update-blog'),
    url(r'blog/post/new$', NewBlogPostView.as_view(), name='new-blog-post'),
    url(r'blog/post/(?P<pk>\d+)/update/$', UpdateBlogPostView.as_view(), name='update-blog-post'),
    url(r'blog/post/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blog-post-details'),
    url(r'blog/post/(?P<pk>\d+)/share/$', ShareBlogPostView.as_view(), name='share-blog-post-with-blog'),
    url(r'blog/post/(?P<post_pk>\d+)/share/to/(?P<blog_pk>\d+)/$',
        SharePostWithBlog.as_view(), name='share-post-with-blog'),
    url(r'blog/post/(?P<post_pk>\d+)/stop/share/to/(?P<blog_pk>\d+)/$',
        StopSharingPostWithBlog.as_view(), name='stop-sharing-post-with-blog'),
]
