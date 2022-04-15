import time
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import get_team_list, get_results, insert_result
from .forms import ResultsForm, UserPasswordForm
from pages.common.views import NSFFPageView

TURKEY_BOWL_HOME = "/turkey-bowl/"
TURKEY_BOWL_INFO = "/turkey-bowl/info/"
TURKEY_BOWL_TEAMS = "/turkey-bowl/teams/"
TURKEY_BOWL_RESULTS = "/turkey-bowl/results/"
TURKEY_BOWL_SCHEDULE = "/turkey-bowl/schedule/"
TURKEY_BOWL_DONATIONS = "/turkey-bowl/clothing-and-hygiene-drive/"
TURKEY_BOWL_RESULTS_MANAGEMENT = "/turkey-bowl/results-management/"
TURKEY_BOWL_PICTURES = "/turkey-bowl/pictures/"
TURKEY_BOWL_SECTIONS = {"Home": TURKEY_BOWL_HOME, "Info": TURKEY_BOWL_INFO, "Clothing/Hygiene Drive": TURKEY_BOWL_DONATIONS, "Teams": TURKEY_BOWL_TEAMS, "Schedule": TURKEY_BOWL_SCHEDULE, "Results": TURKEY_BOWL_RESULTS, "Results Manager": TURKEY_BOWL_RESULTS_MANAGEMENT, "Pictures": TURKEY_BOWL_PICTURES}

class TurkeyBowlPageView(NSFFPageView):

    def __init__(self, tb_subsection, template, pageTitle, pageDescription):
        super().__init__("Turkey Bowl", template, pageTitle, pageDescription)
        self._tb_subsection = tb_subsection

    def get_additional_context(self):
        return {"tb_sections": TURKEY_BOWL_SECTIONS, "tb_subsection":self._tb_subsection, **self.get_turkey_bowl_context()}

    def get_turkey_bowl_context(self):
        return {}


class TurkeyBowlHomeView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Home", "turkey_bowl/home.html", "NSFF Turkey Bowl Home", "Home page for NSFF Turkey Bowl")


class TurkeyBowlPicturesView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Pictures", "turkey_bowl/pictures.html", "NSFF Turkey Bowl Pictures", "Pictures from NSFF Turkey Bowl")


class TurkeyBowlInfoView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Info", "turkey_bowl/info.html", "NSFF Turkey Bowl Info", "Information about NSFF Turkey Bowl")


class TurkeyBowlDonationsView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Clothing/Hygiene Drive", "turkey_bowl/donations.html", "NSFF Turkey Bowl Clothing + Hygiene Drive", "During the NSFF Turkey Bowl, we will be running a clothing and hygiene drive for some of the students of Ingraham High School")


class TurkeyBowlResultsView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Results", "turkey_bowl/results.html", "NSFF Turkey Bowl Results", "Results of this year's NSFF Turkey Bowl")

    def get_turkey_bowl_context(self):
        return {"results": [("Round 1", "round1", get_results(1)), ("Round 2", "round2", get_results(2)), ("Championship", "round3", get_results(3))]}
#        return {"results": {"Round 1": get_results(1), "Round 2": get_results(2), "Championship": get_results(3)}}


class TurkeyBowlResultsManagementView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Results Manager", "turkey_bowl/results-management.html", "NSFF Turkey Bowl Results Management", "Turkey Bowl Results Management")

    def get_turkey_bowl_context(self):
        return {"form": ResultsForm()}

    def post(self, request, *args, **kwargs):
        form = ResultsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            insert_result(data['round_num'], data['game_num'], data['winner'], data['loser'], data['winner_score'], data['loser_score'])
            time.sleep(2)
            return HttpResponseRedirect("/turkey-bowl/results/")

        return self.get(request, *args, **kwargs)


USERNAME = "nsffTourney"
PASSWORD = "N!s2F#f4"

class TurkeyBowlResultsManagementAccessView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Results Manager", "turkey_bowl/results-management-access.html", "NSFF Turkey Bowl Results Management", "Turkey Bowl Results Management")

    def get_turkey_bowl_context(self):
        return {"form": UserPasswordForm()}

    def post(self, request, *args, **kwargs):
        form = UserPasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            if data['username'] == USERNAME and data['password'] == PASSWORD:
                return HttpResponseRedirect("/turkey-bowl/results-updater/")
            else:
                return HttpResponseRedirect("/turkey-bowl/results-management/")

        return self.get(request, *args, **kwargs)


class TurkeyBowlScheduleView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Schedule", "turkey_bowl/schedule.html", "NSFF Turkey Bowl Schedule", "Schedule for the NSFF Turkey Bowl")


class TurkeyBowlPlannedPicturesView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Planned Pictures", "turkey_bowl/pics_to_take.html", "NSFF Turkey Bowl Pictures", "Pictures for NSFF Turkey Bowl")

    def get_turkey_bowl_context(self):
        return {"pictures_to_take": [
            "Organizers",
            "Captains",
            "Each Team",
            "All Participants",
            "Everyone",
            "All ladies",
            "Winning Team (Champs)",
            "Each MVP Individually",
            "Defensive MVPs",
            "Offensive MVPs",
            "All MVPs",
            "Underdog Teams"
        ]}


class TurkeyBowlTeamsView(TurkeyBowlPageView):

    def __init__(self):
        super().__init__("Teams", "turkey_bowl/teams.html", "NSFF Turkey Bowl Teams", "A view of the different teams that are participating in NSFF Turkey Bowl and the rosters")

    def get_turkey_bowl_context(self):
        num_players = 10
        team_list_dict = get_team_list()
        colors = list(team_list_dict.keys())
        teams_list = []
        captains = [team_list_dict[color][0] for color in colors]
        for i in range(1, num_players):
            teams_list.append([team_list_dict[color][i] for color in colors])
        colors_to_css = {color:color.lower().replace(" ", "-") for color in colors}

        return {"colors": colors, "teams_list": teams_list, "css_colors": colors_to_css, "captains": captains}

