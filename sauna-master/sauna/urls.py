from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('project', include('project.urls')),
    path('reviews', include('reviews.urls')),
    path('proposal', include('proposal.urls')),
    path('', include('main.urls')),
    path('catalog', include('catalog.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)