from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import e_handler404, e_handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = e_handler404
handler500 = e_handler500