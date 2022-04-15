from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

#NAV_LINKS = {"Home": "/", "Turkey Bowl": "/turkey-bowl/", "About": "/about/", "Contact": "/contact/"}
NAV_LINKS = {"Home": "/", "Turkey Bowl": "/turkey-bowl/"}

class NSFFPageView(View):

    def __init__(self, active_section, template, pageTitle="North Seattle Flag Football", pageDescription="Page for NSFF"):
        self._active_section = active_section
        self._template = template
        self._pageTitle = pageTitle
        self._pageDescription = pageDescription

    def get(self, request, *args, **kwargs):
        return render(request, self._template, context={"nav_links": NAV_LINKS, "active_section": self._active_section, "pageTitle": self._pageTitle, "pageDescription": self._pageDescription, **self.get_additional_context()})

    def get_additional_context(self):
        return {}

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect("/")

