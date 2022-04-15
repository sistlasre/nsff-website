from django.shortcuts import render
from django.views.generic import TemplateView
from pages.common.views import NSFFPageView

class HomePageView(NSFFPageView):

    def __init__(self):
        super().__init__("Home", "index.html", "North Seattle Flag Football Home", "Home page for North Seattle Flag Football")
