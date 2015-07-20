from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import IndexPageView

urlpatterns = patterns('',
                       url(r'^$', IndexPageView.as_view(), name="index"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^accounts/', include('borrower.urls')),
                       )
