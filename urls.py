from django.conf.urls.defaults import *
from django.contrib import admin
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__),'templates/tiny_mce').replace('\\','/')}),
    (r'^search/$', 'search.views.search'),

    # weBlog
    (r'^blog/categories/', include('blog.urls.categories')),
    (r'^blog/links/', include('blog.urls.links')),
    (r'^blog/tags/', include('blog.urls.tags')),
    (r'^blog/', include('blog.urls.entries')),
    #(r'', include('django.contrib.flatpages.urls')),

    (r'^vote/$', 'voteform.views.checked'),
    (r'^show-result/$', 'voteform.views.show'),
    (r'^code/$', 'voteform.views.invite_codes'),
)

