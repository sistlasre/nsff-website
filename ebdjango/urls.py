"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include('pages.home_page.urls')), 
   url(r'^turkey-bowl/', include('pages.turkey_bowl.urls')), 
   url(r'^bunny-bowl/', include('pages.bunny_bowl.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
