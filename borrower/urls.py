from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^profile/$', 'borrower.views.borrower'),
                       )
