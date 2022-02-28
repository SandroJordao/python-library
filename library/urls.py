from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

router = DefaultRouter()
router.register(r'authors', views.AuthorsApi)
router.register(r'books', views.BooksApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
