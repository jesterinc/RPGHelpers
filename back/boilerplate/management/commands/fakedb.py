from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User 

from random import randint
from faker import Faker
import random

from administrator.models import *
from comuni.models import *
from ordini_professionali.models import *
from consulenti.models import *
from consulenze.models import *


class Command(BaseCommand):
  help = 'Fill DB with faked values'

  def handle(self, *args, **options):

    fake = Faker('it_IT')

    """
    for index in range(0,5):

      user = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': f'admin{index}',
        'username': f'admin{index}',
      }

      user = User.objects.create(**user)

      administrator = {
        'user_id': user.id,
        'commissione': CCTTS().pick_random_cctts(),
        'is_superadmin': False,
        'attivo': True,
      }

      Administrator.objects.create(**administrator)
    """

    """
    for index in range(0,500):

      try:

        citta = Citta.objects.get(citta=fake.city())

      except Citta.DoesNotExist:

        citta = Citta.objects.get(citta='Bologna')

      finally:

        provincia = Province.objects.get(pk=citta.provincia_id)
        regione = Regioni.objects.get(pk=provincia.regione_id)

      tipo = 'con'

      if randint(0, 10) > 7:
      
        tipo = 'com'
      
      specializzazioni = ",".join(fake.bs().split(" "))

      consultant = {
        'cancellato': False,
        'citta': citta,
        'codice_fiscale': fake.vat_id(),
        'cognome': fake.last_name(),
        'commissione': CCTTS().pick_random_cctts(),
        'condanne_penali': False,
        'ct_registrazione': CCTTS().pick_random_cctts(),
        'curriculum_vitae': None,
        'data_esclusione': None,
        'data_nascita': fake.date_of_birth(),
        'data_registrazione': fake.date(),
        'indirizzo': fake.address(),
        'luogo_nascita': fake.city(),
        'nome': fake.first_name(),
        'ordine_professionale': OrdiniProfessionali().pick_random_order(),
        'provincia': provincia,
        'regione': regione,
        'registrazione_espirata': False,
        'sanzioni_disciplinari': False,
        'specializzazioni': specializzazioni,
        'tipo': tipo,
        'curriculum_vitae': fake.file_name(),
      }

      consulente = Consulenti.objects.create(**consultant)

      titolo_studio = {
        'consulente': consulente,
        'in_data': fake.date(),
        'titolo_di_studio': fake.words(3),
        'voto_conseguito': randint(36,110),
      }

      TitoliDiStudio.objects.create(**titolo_studio)

      contatto = {
        'consulente': consulente,
        'telefono': fake.phone_number(),
        'cellulare': fake.phone_number(),
        'email_pec': fake.ascii_company_email(),
        'email_peo': fake.ascii_email(),
      }

      Contatti.objects.create(**contatto)

      titolo_studio = {
        'consulente': consulente,
        'in_data': fake.date(),
        'titolo_di_studio': f"{fake.word()} {fake.word()} {fake.word()}",
        'voto_conseguito': randint(36,110),
      }

      TitoliDiStudio.objects.create(**titolo_studio)

    for consulente in Consulenti.objects.all():

      allegati = {
        'atto_di_nascita': fake.file_name(),
        'certificato_casellario_giudiziario': fake.file_name(),
        'certificato_di_residenza': fake.file_name(),
        'certificato_iscrizione_associazione_professionale': fake.file_name(),
        'consulente': consulente,
        'titoli_atti_dimostrare_capacita_tecnica': fake.file_name(),
      }

      Allegati.objects.create(**allegati)
    """

    commissioni = CCTTS.objects.all()
    consulenti = Consulenti.objects.all()

    for index in range(0,100):

      commissione = commissioni[random.randint(0,len(commissioni)-1)]
      consulente = consulenti[random.randint(0,len(consulenti)-1)]

      consulenza = {
        'acconto': float(random.randint(0,250)),
        'ammontare': float(random.randint(0,1000)),
        'commissione': commissione,
        'consulente_assegnato': consulente,
        'data_assegnazione': fake.date_this_year(),
        'data_consegna_consulenza': fake.date_this_year(),
        'data_creazione': fake.date_between(),
        'data_fine_consulenza': fake.date_this_year(),
        'motivazione': fake.paragraphs(1),
        'richiesta_di_estensione': fake.date_this_year(),
        'richiesta_giudice': fake.paragraphs(1),
        'saldo': float(random.randint(0,1000)),
        'soggetto': fake.job(),
        'stato': settings.STATUSES[random.randint(0,len(settings.STATUSES)-1)][0],
      }

      print(f"\n\nconsulenza {consulenza}\n\n")

      Consulenze.objects.create(**consulenza)




