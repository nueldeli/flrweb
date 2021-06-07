"""flrweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, AboutView, OrganizationView, WdimView, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('about/', AboutView.as_view(), name='about'),
    path('organization/', OrganizationView.as_view(), name='organization'),
    path('why-does-it-matter/', WdimView.as_view(), name='wdim'),
    path('blog/', include('blog.urls')),
    path('data/', include('dms.urls')),
    path('planting/', include('planting.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('membership/', include('django.contrib.auth.urls')),
    path('membership/', include('membership.urls')),
	path('', include('subscription.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
