from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'decisions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(subsession):
        import random
        for player in subsession.get_players():
            player.time_pressure = random.choice([True, False])
            print('set time_pressure to', player.time_pressure)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_pressure = models.BooleanField()

    situation1_personal = models.IntegerField(
        choices=[(1, "Robar el 80% de las ganancias  del individuo B."),
                 (2, "No robar el 80% de las ganancias del individuo B.")],
        widget=widgets.RadioSelect)
    
    def candidates_random(player):
        choices = [
            [1, 'Gustavo Petro'],
            [2, 'Federico Gutiérrez'],
            [3, 'Sergio Fajardo'],
            [4, 'Enrique Gómez'],
            [5, 'Ingrid Betancourt'],
            [6, 'John Milton Rodríguez'],
            [7, 'Luis Pérez'],
            [8, 'Rodolfo Hernández'],
            [9, 'Voto en Blanco'],
            [10, 'No voy a votar']
        ]
        random.shuffle(choices)
        return choices

    candidates = models.IntegerField(
        choices=[],
        widget=widgets.RadioSelect(),
        label=""
    )
# el randomizador de opciones tiene que estar afuera del objeto Player!
def situation1_personal_choices(Player):
    choices = [(1, "Robar el 80% de las ganancias  del individuo B."),
             (2, "No robar el 80% de las ganancias del individuo B.")]
    random.shuffle(choices)
    return choices



# PAGES
class a04_opinion(Page):
    form_model = 'player'
    form_fields = [#'candidates',
                   #'fruit'
                  'situation1_personal']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [a04_opinion]
