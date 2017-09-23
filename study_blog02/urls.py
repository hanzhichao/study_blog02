from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^blog/article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article'),
    url(r'^blog/category/(?P<cate_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^blog/tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', ArchiveView.as_view(), name='archive'),
]