from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import books.views
import cmdb.views
# from mysite import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', books.views.hello),
    # url(r'^contact/thanks/$', books.views.hello),
    # url(r'^d/$', books.views.display_meta),
    # url(r'^search/$', books.views.search),
    # url(r'^c/$', books.views.contact),
)

urlpatterns += patterns('books.views',
    url(r'contact/thanks/$', 'hello'),
    url(r'^$', 'hello'),
    url(r'^d/$', 'display_meta'),
    url(r'^search/$', 'search'),
    url(r'^c/$', 'contact'),
    # url(r'^a/(?P<year>\d{4})$', 'year_archive'),
    # url(r'^a/(?P<year>\d{4})/(?P<month>\{2})$/', 'month_archive'),
    # url(r'^foo/$', 'foobar_view', {'template_name': 'template1.html'}),
    # url(r'^bar/$', 'foobar_view', {'template_name': 'template2.html'}),
)

urlpatterns += patterns('cmdb.views',
    url(r'login$', 'login'),
    url(r'ip$', 'IpList'),
    url(r'host$', 'HostList'),
    url(r'vm', 'VmList'),
    )

# if settings.DEBUG:
#     urlpatterns += patterns('',
#     url(r'^debiginfo/$', views.debug),
#     )