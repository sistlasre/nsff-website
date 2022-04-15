from django import forms

COLOR_CHOICES = ['Heliconia', 'Red', 'Gold', 'Turquoise', 'Purple', 'Charcoal', 'Lime Green', 'Ice Gray']
COLOR_CHOICES_TUPLES = [(color, color) for color in COLOR_CHOICES]

class ResultsForm(forms.Form):
    round_num = forms.IntegerField(label="Round", min_value=1, max_value=3)
    game_num = forms.IntegerField(label="Game", min_value=1, max_value=4)
    winner = forms.ChoiceField(label="Winning Team", choices=COLOR_CHOICES_TUPLES)
    winner_score = forms.IntegerField(label="Winning Team's Score")
    loser = forms.ChoiceField(label="Losing Team", choices=COLOR_CHOICES_TUPLES)
    loser_score = forms.IntegerField(label="Losing Team's Score")

class UserPasswordForm(forms.Form):
    username = forms.CharField(label="User Name")
    password = forms.CharField(label="Password")

