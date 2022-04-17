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
    for p in subsession.get_players():
        p.treatment = next(treatment)
        p.order_politics = next(order)
        print('Treatment', p.treatment)
        print('Order', p.order_politics)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    r_seed = models.FloatField()
    treatment = models.IntegerField()
    order_politics = models.IntegerField()

    compromise = models.IntegerField()

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
        choices=[[0, "Fajardo"], [1, "Petro"]],
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

    secure = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, "Estaba muy seguro/a de mis respuestas"],
            [2, "Estaba algo seguro/a de mis respuestas"],
            [3, "Estaba algo inseguro/a de mis respuestas"],
            [4, "Estaba muy inseguro/a de mis respuestas"]
        ],
        label="En resumen, ¿qué tan seguro se siente de las respuestas que acaba de dar en la sesión anterior?"
    )

    will_consider = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, 'Nada'],
            [2, 'Poco'],
            [3, 'En parte'],
            [4, 'Mucho']
        ],
        label="¿En qué medida cree que los candidatos van a tener en consideración los resultados de este estudio?"
    )

    should_consider = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[
                [1, 'Nada'],
                [2, 'Poco'],
                [3, 'En parte'],
                [4, 'Mucho']
                 ],
        label="¿En qué medida cree que los candidatos deberían tener en consideración los resultados de este estudio?"
    )

    spectrum = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    age = models.IntegerField(
        label="¿Cuál es su edad?"
    )
    sex = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, 'Femenino'],
            [2, 'Masculino'],
            [3, 'Prefiero no decirlo']
                 ],
        label='¿Cuál es su sexo?'
    )
    ses = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6],
        label="¿De acuerdo a la factura de sus servicios, ¿en qué estrato se encuentra su vivienda?"
    )

    labor_status = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, "Activo"],
            [2, "En búsqueda de empleo"],
            [3, "Jubilado"],
            [4, "Estudiante"],
            [5, "Otro (no trabaja/no busca trabajo/no estudia, responsable del hogar, discapacitado no trabajador)"]
        ],
        label="¿Cuál de las siguientes situaciones describe mejor su situación laboral actual?"
    )


    schoolar = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, "Primaria o menor"],
            [2, "Secundaria"],
            [3, "Algunos años de universidad o formación profesional de grado superior"],
            [4, "Universidad o formación profesional de grado superior"],
            [5, "Posgrado (Especialización, Máster, Doctorado, etc)"]
        ],
        label="¿Cuál es su máximo nivel de estudios finalizado?"
    )

    marital = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, "Soltero/a"],
            [2, "Casado/a o en unión civil"],
            [3, "Divorciado/a o viudo/a"]
        ],
        label="¿Cuál es su estado civil?"
    )

    home_size = models.IntegerField(
        label="¿Cuántas personas viven normalmente en su hogar (incluyéndose usted)? "
    )

    fluid_1 = models.IntegerField(label="Un bate y una pelota cuestan $1.10 en total. "
                                      "El bate cuesta $1.00 más que la pelota. ¿Cuántos "
                                      "centavos cuesta la pelota?")

    fluid_2 = models.IntegerField(
        label="Si 5 máquinas se demoran 5 minutos para hacer 5 artículos, "
              "¿cuántos minutos les tomaría a 100 máquinas hacer 100 artículos?"
    )

    fluid_3 = models.IntegerField(
        label="En un lago hay un segmento de almohadillas de lirios y "
              "cada día ese segmento dobla su tamaño. Si el segmento tarda"
              " 48 días en cubrir el lago, ¿cuántos días tardará el segmento en "
              "cubrir la mitad del lago?"
    )

    risk = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    intemporal = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label="En comparación con los demás, ¿es usted "
              "una persona que generalmente está dispuesta a "
              "renunciar a algo hoy para beneficiarse de eso "
              "en el futuro o no está dispuesto a hacerlo? Por"
              " favor utilice una escala de 0 a 10, donde 0 "
              "significa que usted es una persona que “no está "
              "para nada dispuesta a renunciar a algo hoy” y 10 "
              "significa que usted es una persona que “está "
              "completamente dispuesta a renunciar a algo hoy”."
              " También puede utilizar los valores intermedios "
              "para indicar donde se encuentra en la escala."
    )

    positive_expectation = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label="¿Hasta qué punto le describe como personal el"
              " siguiente enunciado? Mientras no esté convencido"
              " de lo contrario, asumo que las personas "
              "solo tienen buenas intenciones. Por favor "
              "utilice una escala de 0 a 10, donde 0 significa"
              " “no me describe en absoluto” y 10 significa "
              "“me describe perfectamente”. También puede "
              "utilizar los valores intermedios para indicar"
              " donde se encuentra en la escala."
    )


    altruism = models.IntegerField(
        choices=[
            (1, '100.000 (10%)'),
            (2, '200.000 (20%)'),
            (3, '300.000 (30%)'),
            (4, '400.000 (40%)'),
            (5, '500.000 (50%)'),
            (6, '600.000 (60%)'),
            (7, '700.000 (70%)'),
            (8, '800.000 (80%)'),
            (9, '900.000 (90%)'),
            (10, '1.000.000 (100%)'),
        ],
        widget=widgets.RadioSelect,
        label="Imagine la siguiente situación: usted ha ganado 1.000.000 de pesos en una lotería. "
              "Considerando su situación actual, ¿cuánto estaría dispuesto a donar a buenas "
              "causas?"
    )

    botella = models.IntegerField(
        label='Imagine la siguiente situación: usted está de compras en una ciudad que no es familiar'
              ' para usted y se da cuenta de que perdió el camino. Usted decide preguntarle a un extraño '
              'por indicaciones. El extraño ofrece llevarlo en su carro al destino que usted tenía. '
              'El viaje dura cerca de 20 minutos y le cuesta al extraño 20.000 pesos. El extraño no '
              'desea dinero por haberlo llevado. Usted lleva seis botellas de vino con usted. '
              'La botella más barata cuesta 5.000 pesos, la botella más cara cuesta 30.000 pesos. '
              'Usted decide darle una de sus botellas al extraño como agradecimiento por el favor.'
              ' ¿Cuál botella le daría?',
        choices=[
            (1, 'Botella de 5.000 pesos'),
            (2, 'Botella de 10.000 pesos'),
            (3, 'Botella de 15.000 pesos'),
            (4, 'Botella de 20.000 pesos'),
            (5, 'Botella de 25.000 pesos'),
            (6, 'Botella de 30.000 pesos')],
        widget=widgets.RadioSelect
    )

    self_perception_justicia = models.IntegerField(
        label = '¿Cómo se ve a usted mismo? ¿Es una persona que generalmente está dispuesta a castigar comportamientos injustos, incluso, si esto es costoso para usted?'
                'Por favor use una escala de 0 a 10, donde 0 significa que usted “no está dispuesto a incurrir en costos para castigar comportamientos injustos” y 10 significa que usted “está muy dispuesto a incurrir en costos para castigar comportamientos injustos”. '
                'También puede usar los valores intermedios para indicar dónde se encuentra en la escala.',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect
        )

    religion = models.IntegerField(
        label='¿Cuál es su religión?',
        choices=[
            [1, 'Judaísmo'],
            [2, 'Catolicismo'],
            [3, 'Evangélico - Protestante'],
            [4, 'Islamismo'],
            [5, 'Hinduismo'],
            [6, 'Budismo'],
            [7, 'Mormones'],
            [8, 'Confucianismo'],
            [9, 'Pentecostales'],
            [10, 'Ninguna'],
            [11, 'Otra']
            ],
        widget=widgets.RadioSelect
    )

    frequency_religion = models.IntegerField(
        label='¿Normalmente con qué frecuencia asiste a una función religiosa?',
        choices=[1, 2, 3, 4, 5, 6],
        widget=widgets.RadioSelect
    )

    poverty = models.IntegerField(
        label='Entre los siguientes dos, ¿cuál factor cree que sea más'
              ' importante para que una persona se encuentre en estado de pobreza?',
        choices=[
                 [1, "Falta de esfuerzo y compromiso laboral por parte de la persona"],
                 [2, "Suerte o eventos que no están en control de la persona"]
        ],
        widget=widgets.RadioSelect
    )

    impuesto = models.IntegerField(
        label="¿Qué tan de acuerdo está con que el Gobierno tenga que reducir "
              "las diferencias entre ricos y pobres, de pronto subiendo los impuestos "
              "para los ricos o proveyendo asistencia a los ingresos de los más pobres?"
              " Por favor, indique que tan de acuerdo está marcando un número"
              " de uno a cinco en la escala de abajo, donde uno indica “estoy totalmente "
              "en desacuerdo” y cinco indica “estoy totalmente de acuerdo”.",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    distribution = models.IntegerField(
        label="¿Piensa que la distribución del ingreso en Colombia es equitativa?"
              " ¿o piensa que el dinero y la riqueza de este país tienen que repartirse"
              " entre un número mayor o menor de personas?",
        choices=[
            [1, "La distribución es equitativa"],
            [2, "Dinero y riqueza tendrían que repartirse de manera más igualitaria"],
            [3, "Dinero y riqueza tendrían que repartirse de manera menos igualitaria"]
        ],
        widget=widgets.RadioSelect
    )

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
class a01_intro(Page):
    pass

class a02_consent(Page):
    pass

class a03_note(Page):
    form_model = 'player'
    form_fields = ['compromise']

class a04_opinion(Page):
    form_model = 'player'
    form_fields = ['candidates']

class a05_opinion(Page):
    form_model = 'player'
    form_fields = ['pe_fi', 'pe_fa', 'fa_fi']

    @staticmethod
    def vars_for_template(player):
        seed = random.random()
        return dict(
            seed=seed,
        )

class a06_info(Page):
    pass

class a07_politica(Page):
    form_model = 'player'

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

class a13_questionnaire(Page):
    form_model = 'player'
    form_fields = ['secure', 'will_consider', 'should_consider']

    @staticmethod
    def vars_for_template(player):
        seed = random.random()
        return dict(
                seed=seed,
            )

class a14_questionnaire(Page):
    form_model = 'player'
    form_fields = ['home_size',
    'marital', 'schoolar', 'labor_status', 'ses', 'sex', 'age', 'spectrum']

class a15_questionnaire(Page):
    form_model = 'player'
    form_fields = [
            'distribution', 'impuesto', 'poverty', 'frequency_religion', 'religion',
            'self_perception_justicia', 'botella', 'altruism', 'positive_expectation',
            'intemporal', 'risk', 'fluid_3', 'fluid_2', 'fluid_1'
        ]



page_sequence = [
                 a01_intro,
                 a02_consent,
                 a03_note,
                 a04_opinion,
                 a05_opinion,
                 a06_info,
                 a07_politica,
                 a08_politica,
                 a09_politica,
                 a10_politica,
                 a11_send,
                 a12_send,
                 a13_questionnaire,
                 a14_questionnaire,
                 a15_questionnaire
                    ]
