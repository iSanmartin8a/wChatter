from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from chatter_web.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('chatter/', include('chatter_web.urls')),
]

urlpatterns += [
    path('', index, name='index'),
    ## URLS de django-debug-toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]