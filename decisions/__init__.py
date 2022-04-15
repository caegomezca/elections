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
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    situation1_personal = models.IntegerField(
        choices=[(1, "Robar el 80% de las ganancias  del individuo B."),
                 (2, "No robar el 80% de las ganancias del individuo B.")],
        widget=widgets.RadioSelect)

    # Esto es para randomizar las choices
    def situation1_personal_choices(self):
        choices = [(1, "Robar el 80% de las ganancias  del individuo B."),
                   (2, "No robar el 80% de las ganancias del individuo B.")]
        random.shuffle(choices)
        return choices






    fruit = models.StringField(
        choices = [
            [1, 'Apple'],
            [2, 'Kiwi'],
            [3, 'Mango'],
        ],
        widget=widgets.RadioSelect(),
        label=""
    )

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


# PAGES
class a04_opinion(Page):
    form_model = 'player'
    form_fields = [#'candidates',
                   #'fruit'
                  'situation1_personal']



    #@staticmethod
    #def vars_for_template(player):
    #    import random
    #    choices = [
    #        [1, 'Apple'],
    #        [2, 'Kiwi'],
    #        [3, 'Mango'],
    #    ]
    #    random.shuffle(choices)
    #    return dict(fields=choices)






class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [a04_opinion]
