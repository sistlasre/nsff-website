from django.urls import path
from .views import *

urlpatterns = [
    path('', TurkeyBowlHomeView.as_view()),
    path('info/', TurkeyBowlInfoView.as_view()),
    path('teams/', TurkeyBowlTeamsView.as_view()),
    path('results/', TurkeyBowlResultsView.as_view()),
    path('results-management/', TurkeyBowlResultsManagementAccessView.as_view()),
    path('results-updater/', TurkeyBowlResultsManagementView.as_view()),
    path('schedule/', TurkeyBowlScheduleView.as_view()),
    path('pictures/', TurkeyBowlPicturesView.as_view()),
    path('clothing-and-hygiene-drive/', TurkeyBowlDonationsView.as_view()),
    path('planned-pictures/', TurkeyBowlPlannedPicturesView.as_view()),
]
