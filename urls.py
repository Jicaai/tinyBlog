from django.conf.urls.defaults import *
import os.path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^tinyCMS/', include('tinyCMS.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

        
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__),'templates/tiny_mce').replace('\\','/')}),
    #(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/realjld/tiny/mysite/tinyCMS/tiny_mce'}),
    (r'^search/$', 'search.views.search'),

    # weBlog
    (r'^blog/categories/', include('blog.urls.categories')),
    (r'^blog/links/', include('blog.urls.links')),
    (r'^blog/tags/', include('blog.urls.tags')),
    (r'^blog/', include('blog.urls.entries')),
    #(r'^blog/', include('blog.urls')),
    #(r'', include('django.contrib.flatpages.urls')),
)

