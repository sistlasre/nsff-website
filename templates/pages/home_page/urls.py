# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from .views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]
