from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'decisions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TREATMENTS = [0, 1, 2, 3, 4, 5, 6, 7]
    ORDER_POLITICS = [0, 1, 2, 3]

#                    Treatments
#              No name   |    Name    |
#Control   |     0       |      1     |
#Echo      |     2       |      3     |
#Opposite  |     4       |      5     |
#Polarized |     6       |      7     |

# ORDER POLITICS             ORDER 0      ORDER 1     ORDER 2      ORDER 3
#POLITICA DISONANTE 1          1            2           2             1
#POLITICA DISONANTE 2          2            1           1             2
#POLITICA ABSURDA 1            1            1           2             2
#POLITICA ABSURDA 2            2            2           1             1


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    treatment = itertools.cycle(C.TREATMENTS)
    order = itertools.cycle(C.ORDER_POLITICS)
    for player in subsession.get_players():
        player.treatment = next(treatment)
        player.order_politics = next(order)
        print('Treatment', player.treatment)
        print('Order', player.order_politics)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.IntegerField()
    order_politics = models.IntegerField()

    candidates = models.IntegerField(
        choices=[
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
        ],
        widget=widgets.RadioSelect,
        label=""
    )

    pe_fi = models.IntegerField(
        choices=[[0, "Petro"], [1, "Fico"]],
        label="¿Petro o Fico?",
        widget = widgets.RadioSelectHorizontal
    )

    pe_fa = models.IntegerField(
        choices=[[0, "Petro"], [1, "Fajardo"]],
        label="¿Fajardo o Petro?",
        widget=widgets.RadioSelectHorizontal
    )

    fa_fi = models.IntegerField(
        choices=[[0, "Fajardo"], [1, "Fico"]],
        label="¿Fajardo o Fico?",
        widget=widgets.RadioSelectHorizontal
    )

#q1a question 1 disonante 1
#q1b questions 2 disonante 1
#q2a question 1 disonante 2
#q2b questions 2 disonante 2

    q1a = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q1b = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q2a = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q2b = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q3a = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q3b = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q4a = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    q4b = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    dictator = models.IntegerField(min=0, max=10)

##########



def candidates_choices(Player):
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

# PAGES
class a04_opinion(Page):
    form_model = 'player'
    form_fields = ['candidates']

class a05_opinion(Page):
    form_model = 'player'
    form_fields = ['pe_fi', 'pe_fa', 'fa_fi']

class a06_info(Page):
    pass

class a07_politica(Page):
    form_model = 'player'
#    form_fields = ['q1a', 'q1b']
    @staticmethod
    def get_form_fields(player):
        if player.order_politics == 0 or player.order_politics == 3:
            return ['q1a', 'q1b']
        else:
            return ['q2a', 'q2b']


class a08_politica(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.order_politics == 0 or player.order_politics == 3:
            return ['q2a', 'q2b']
        else:
            return ['q1a', 'q1b']


class a09_politica(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.order_politics == 0 or player.order_politics == 1:
            return ['q3a', 'q3b']
        else:
            return ['q4a', 'q4b']


class a10_politica(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.order_politics == 0 or player.order_politics == 1:
            return ['q4a', 'q4b']
        else:
            return ['q3a', 'q3b']


class a11_send(Page):
    pass

class a12_send(Page):
    form_model = 'player'
    form_fields = ['dictator']


class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [#a05_opinion,
                 #a06_info,
                 #a07_politica,
                 #a08_politica,
                 #a09_politica,
                 #a10_politica,
                 a11_send,
                a12_send,
                    ]
