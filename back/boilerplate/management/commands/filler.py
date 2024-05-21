from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings

import random
from random import randrange
from faker import Faker

from clienti.models import Clienti
from pratiche.models import Pratiche
from scadenze.models import Scadenze
from pratiche.models import Udienze
from pratiche.models import Adempimenti
from pratiche.models import Scadenze
from pratiche.models import DatiVari

from .nomi import nomi, cognomi
from .comuni import comuni
from .locazioni import locazioni
from .prefissi import prefissi
from .province import province
from .emails import emails


class Command(BaseCommand):
  help = 'Filler of dummy data to mockup db'

  def compose_name(self):

    return f"{nomi[randrange(0,len(nomi)-1)]}"

  def compose_surname(self):

    return f"{cognomi[randrange(0,len(cognomi)-1)]}"

  def compose_fiscal_code(self, nome, cognome):

    return f"{nome[:3]}{cognome[0:3]}21H45R123F"

  def compose_address(self):

    return f"{locazioni[int(randrange(0,len(locazioni)-1))]} {indirizzi[int(randrange(0,len(indirizzi)-1))]}, {int(randrange(1, 101))}"

  def comune(self):

    try:

      count = Cities.objects.count()
      city = Cities.objects.all()[randint(0, count - 1)]
      province = Provinces.objects.get(pk=city.province_id)
      region = Regions.objects.get(pk=province.region_id)

      return {"city": city.city, "cap": city.cap ,"province": province.province, "region": region.region}

    except Exception as ex:

      print(f"comune Exception {ex}")

  def provincia(self):

    return province[int(randrange(0,len(province)-1))]

  def prefisso(self):

    return prefissi[int(randrange(0,len(prefissi)-1))]

  def telefono(self):

    return ''.join([str(random.randint(0, 9)) for i in range(7)])

  def compose_email(self,first_name,last_name):

    try:

      return f"{first_name[0]}.{last_name}@{emails[randrange(0,len(emails)-1)]}"

    except Exception as ex:

      print(f"comune Exception {ex}")


  def numero_pratica(self):

    return f"P{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}/{random.randint(0,9)}{random.randint(0,9)}"

  def random_text(self):

    fake = Faker()
    
    return fake.sentence()

  def handle(self, *args, **options):

    faker = Faker()

    #for index in range(0,1000):

    #  try:

    #    nome = self.compose_name()
    #    cognome = self.compose_surname()
    #    telefono = f"{self.prefisso()}{self.telefono()}"
    #    cliente = Clienti(nome=nome,cognome=cognome,codice_fiscale=self.compose_fiscal_code(nome, cognome),telefono=telefono,email=self.compose_email(nome, cognome),partita_iva='')
    #    cliente.save()

    #  except Exception as ex:

    #    print(f"Exception {ex} {cliente}")

    #for index in range(0,100):

      
    #  pratica = Pratiche(
    #    numero_pratica=self.numero_pratica(),
    #    data_lettera_intervento=faker.date(),
    #    anno=faker.date()[:4],
    #    tipo='001',
    #    cliente_id=randrange(0,1001),
    #    tipo_prescrizione='002',
    #    data_scadenza=faker.date(),
    #    testo=self.random_text(),
    #    importante=faker.boolean()
    #  )

    #  pratica.save()

    #name = self.compose_name()
    #surname = self.compose_surname()
    #utente = Utenti(first_name=name, last_name=surname, login=f"{first_name[0]}_{last_name}", email=compose_email(name, surname),password='',tenant_id=1)
    #utente.save()

    #tipo_scadenza = TipiScadenze(tipo_scadenza='Scadenza 1',attiva=True)
    #tipo_scadenza.save()

    #tipo_tenant = TipiTenants(tenant='',tipo_scadenza_id=1,periodicita_scadenza='')
    #tipo_tenant.save()

    #tenant = Tenants(user_id=1,ragione_sociale='Una ditta a caso SpA',partita_iva='123456789014',logo='nologo.png')
    #tenant.save()

    #for index in range(0,240):

    #  scadenza = Scadenze(
    #    tipo_scadenza=faker.text()[:50],
    #    data_scadenza=faker.date(),
    #    pratica_id=random.randint(1,105),
    #    data_sinistro=faker.date(),
    #  )

    #  scadenza.save()


    for index in range(0,240):

    #  udienza = Udienze(
    #    pratica_id = random.randint(1,105),
    #    data_udienza = faker.date(),
    #    testo = faker.text()
    #  )
    #  udienza.save()

    #  adempimento = Adempimenti(
    #    pratica_id = random.randint(1,105),
    #    data_adempimento = faker.date(),
    #    testo = faker.text()
    #  )
    #  adempimento.save()

    #  scadenza = Scadenze(
    #    pratica_id = random.randint(1,105),
    #    data_scadenza = faker.date(),
    #    testo = faker.text()
    #  )
    #  scadenza.save()

      dati_vari = DatiVari(
        pratica_id = random.randint(1,105),
        C_P = faker.text(),
        targa_cliente = faker.text()[:7],
        data_sinistro = faker.date(),
        stato = faker.text()[:100],
        archivio_numero = faker.text()[:20],
        assicurazione = faker.text()[:100],
        avvocato = faker.text()[:100],
        provenienza = faker.text()[:100],
        procedimento = faker.text()[:100],
        ufficio_giudizlaie = faker.text()[:100],
        ruolo_generale = faker.text()[:100],
      )
      dati_vari.save()



