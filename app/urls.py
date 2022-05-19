from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('',views.index, name='home'),
    path('services/<int:id>',views.service, name='service'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('projects/<int:id>',views.project, name='project'),
    path('blog/<int:id>',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 