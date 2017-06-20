from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<prod_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^process/$', views.process, name='process'),
    url(r'^add/$', views.add, name='add'),
]

if settings.DEBUG :
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

