from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dictaguarani.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^word/(?P<word>[\w\-]+)/', 'words.views.word_view', name='word_view'),
    url(r'^search/', 'words.views.word_index', name='word_index'),
)
