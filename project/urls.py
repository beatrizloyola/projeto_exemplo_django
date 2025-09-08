from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('forum/', include('forum.urls')),
    path('admin/', admin.site.urls),
]
