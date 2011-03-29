from django.conf.urls.defaults import *

import os.path

from weBlog.views import Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Generic views
entry_info_dict={
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
    }

urlpatterns = patterns('',
    # Example:
    # (r'^tinyCMS/', include('tinyCMS.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

        
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__),'tiny_mce').replace('\\','/')}),
    #(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/realjld/tiny/mysite/tinyCMS/tiny_mce'}),
    (r'^search/$', 'search.views.search'),

    # weBlog
    (r'^weblog/$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict),
    # (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'weBlog.views.entry_detail'),
    (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            'django.views.generic.date_based.object_detail', entry_info_dict),


    # (r'', include('django.contrib.flatpages.urls')),
)
