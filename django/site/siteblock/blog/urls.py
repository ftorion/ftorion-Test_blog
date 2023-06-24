from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("category/<str:slug>", PostBYCategry.as_view(), name="category"),
    path("post/<str:slug>", GetPost.as_view(), name="post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)