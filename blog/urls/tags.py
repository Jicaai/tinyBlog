from django.conf.urls.defaults import *
from tagging.models import Tag
from blog.models import Entry, Link
urlpatterns = patterns('',
                        (r'^$',
                         'django.views.generic.list_detail.object_list',
                         {'queryset': Tag.objects.all()}, 'blog_tag_list'),
                        
                        (r'^entries/(?P<tag>[-\w]+)/$',
                         'tagging.views.tagged_object_list',
                         {'queryset_or_model': Entry,
                          'template_name': 'blog/entries_by_tag.html'}, 'entries_by_tag'),

                        (r'^entries/(?P<tag>[-\w]+)/$',
                         'tagging.views.tagged_object_list',
                         {'queryset_or_model': Link,
                          'template_name': 'blog/links_by_tag.html'}),

                       )
