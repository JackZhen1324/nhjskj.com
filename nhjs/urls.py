from django.conf.urls import patterns, include, url
from django.contrib import admin
from nhjsWeb.views import *
from django.views.generic.base import TemplateView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nhjs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       url(r'^homepage/', home),
                       url('^$', home),
                       url(r'^QiYeJianJie/', TemplateView.as_view(template_name="QiYeJianJie.html")),
)
