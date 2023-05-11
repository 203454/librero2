from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .views import LibrosView


urlpatterns = [
    path('libro/',LibrosView.as_view(), name='libro_list'),
    path('libro/<int:id>',LibrosView.as_view(),name='libro_process'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]