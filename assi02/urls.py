from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('classwork/', include('classwork.urls')),
    path('admin/', admin.site.urls),
]
