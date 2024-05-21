from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings

from django.contrib.auth.models import User
from users.models import *
from geographic_areas.models import *
from verticals.models import *
from leads.models import *
from verticals.models import *
from orders.models import *

from verticals.api.serializers import *
from users.api.serializers import *
from geographic_areas.api.serializers import *



from re import search 
import os
from pathlib import Path

from faker import Faker

from faker.providers import address
from faker.providers import automotive
from faker.providers import bank
from faker.providers import company
from faker.providers import currency
from faker.providers import date_time
from faker.providers import internet
from faker.providers import person
from faker.providers import phone_number
from faker.providers import ssn

import random
import datetime
import decimal
import json
from datetime import date
from dateutil.relativedelta import relativedelta
 

class Command(BaseCommand):
  help = 'Create boilerplating APIView'

  def handle(self, *args, **options):

    fake = Faker('it_IT')

    #for registry in Registry.objects.all():
    #
    #  for index in range(0,random.randrange(1,5)):
    #
    #    city =Cities.objects.order_by('?').first()
    #    PlacesOfInterest.objects.create(registry=registry,city=city,active=True,deleted=False)

    #for area in Areas.objects.all():
    #
    #  for vertical in Verticals.objects.all():
    #
    #    for index in range(0,random.randrange(1,5)):
    #
    #      registry = Registry.objects.order_by('?').first()
    #      vi = VerticalsInterest.objects.create(registry=registry,max_monthly_requests=random.randint(50,70),max_daily_requests=random.randint(3,10),subscribed=True,active=True,deleted=False,details='{}',answers_details='{}')
    #      vi.verticals.add(vertical)
    #      
    #      vi.geographic_areas.add(area)

    #
    # for area in Areas.objects.all():
    #
    #   provinces = Provinces.objects.all()
    #
    #   for index in range(0,random.randrange(1,5)):
    #
    #     province = Provinces.objects.order_by('?').first()
    #     region = Regions.objects.get(pk=province.region_id)
    #     nation = Nations.objects.get(pk=region.nation_id)
    #
    #     area.province.create(province=province)
    #     area.region.create(region=region)
    #     area.nation.create(nation=nation)

    #for province in Provinces.objects.all():
    #
    #  print(province.id)
    #  Areas.objects.create(
    #    area=fake.paragraph(nb_sentences=1)[:20].rsplit(' ', 1)[0],
    #    nation_id=1,
    #    region=Regions.objects.get(pk=province.region_id),
    #    province=province,
    #  )
    #
    #verticals = Verticals.objects.all()
    #areas = Areas.objects.all()
    #
    #for user in Registry.objects.all():
    #
    #  vi = VerticalsInterest.objects.create(
    #    registry=user,
    #    details="",
    #    max_monthly_requests=50,
    #    max_daily_requests=3,
    #    answers_details='{}',
    #    subscribed=True,
    #    active=True,
    #    deleted=False
    #  )
    #
    #  for vert in range(1,random.randint(0,4)):
    #    #    vi.verticals.add(verticals[vert])
    #
    #  for area in range(1,random.randint(0,2)):
    #
    #    vi.geographic_areas.add(areas[area])
    #
    #  vi.save()
    #
    # for vertical in Verticals.objects.all():
    #
    #  for index in range(0,random.randrange(2,6)):
    #
    #    question = fake.paragraph(nb_sentences=1)[:80]
    #    quest = Questions.objects.create(vertical=vertical,question=question,orders=index)
    #        
    #    for index2 in range(1,random.randrange(1,5)):
    #
    #      kind = 'rad'
    #
    #      if random.randint(0,1) == 0:
    #
    #        kind = 'chk'
    #
    #         answer = fake.paragraph(nb_sentences=1)[:80]
    #         answ = Answers.objects.create(question=quest,answer=answer,orders=index,kind=kind)
    #
    """
    for question in Questions.objects.all():

      for index in range(0,random.randrange(1,5)):

        kind = 'rad'

        if random.randint(0,1) == 0:

          kind = 'chk'

        answer = fake.paragraph(nb_sentences=1)[:80]
        answ = Answers.objects.create(question=question,answer=answer,orders=index,kind=kind)
    """




### REGISTRY (users)

    #    for index in range(30, random.randrange(50, 999)):
    #
    #      first_name = fake.first_name()
    #      last_name =  fake.last_name()
    #
    #      user = User.objects.create_user(
    #        username=f"{first_name} {last_name}",
    #        email=fake.ascii_email(),
    #        first_name=first_name,
    #        last_name=last_name,
    #        password="pippo",
    #      )
    #
    #      Registry.objects.create(
    #        user=user,
    #        company=fake.company(),
    #        contact_person=f"{first_name} {last_name}",
    #        address=fake.address(),
    #        vat_number=fake.vat_id(),
    #        active=True,
    #        deleted=False,
    #      )
    #
    #      ### CONTACTS
    #
    #      for index in range(2,random.randrange(2,5)):
    #
    #        kind = settings.CONTACT_TYPES[random.randrange(0, len(settings.CONTACT_TYPES) - 1)][0]
    #        value = ''
    #        
    #        if kind == 'CEL' or kind == 'PHO':
    #
    #          value = f"{fake.area_code()} {fake.phone_number()}"
    #
    #        elif kind == 'EMA':
    #
    #          value = fake.ascii_company_email()
    #
    #        else:
    #
    #          kind = fake.simple_profile()['username']
    #
    #        main_contact = f"{fake.first_name()} {fake.last_name()}"
    #
    #        if(value):
    #
    #          Contacts.objects.create(
    #            registry_id=user.id,
    #            kind=kind[:3],
    #            value=value,
    #            main_contact=main_contact,
    #            active=True,
    #            deleted=False,
    #          )
    #
    ### REGIONS OF INTERESTS
    #regions = Regions.objects.all().order_by('region')    

    #for user in Registry.objects.all():

    #  regions_interest = []

    #  for index in range(1,random.randrange(1,5)):

    #    region = regions[random.randrange(0, len(regions)-1)].id
        
    #    if not region in regions_interest:

    #      RegionsInterest.objects.create(
    #        registry_id=user.id,
    #        region_id=region,
    #        active=True,
    #        deleted=False
    #      )

    ### CUSTOMERS COMMENTS
    #for user in Registry.objects.all():
    #
    #  for comment in range(1,random.randint(0,4)):
    #
    #    CustomersComments.objects.create(
    #      customer_id=user.id,
    #      comment=fake.paragraph(nb_sentences=1),
    #      published=random.choice([True, False]),
    #      evaluation=random.choice([0,1,2,3,4,5]),
    #      accepted_conditions=True,
    #      customer_email=fake.ascii_free_email(),
    #      customer_name=f"{fake.first_name()} {fake.last_name()}",
    #      done_jobs_with=random.choice([True,False]),
    #      deleted=False,
    #    )


    ### LEADS COMMENTS
    for user in Registry.objects.all():
    
      for comment in range(1,random.randint(0,4)):
    
        LeadsComments.objects.create(
          customer_id=user.id,
          comment=fake.paragraph(nb_sentences=1),
          evaluation=random.choice([0,1,2,3,4,5]),
          published=random.choice([True, False]),
          deleted=False,
        )


    ### VERTICALS

    #verticals_list = [
    #  'Impianti Fotovoltaici',
    #  'Finanziamenti',
    #  'Cessione del Quinto',
    #  'Depurazione',
    #  'Formazione',
    #  'Corsi di lingua',
    #  'Ristrutturazioni',
    #  'Salute e benessere',
    #  'Caldaie e Stufe',
    #  'Infissi',
    #  'Risparmio Energetico',
    #  'Edilizia',
    #  'Traslochi',
    #]
    
    #for vertical in verticals_list:

    #  Verticals.objects.create(
    #    name=vertical,
    #    description=fake.paragraph(nb_sentences=1),
    #    special_fields={},
    #    active=random.choice([True, False]),
    #    deleted=False,
    #  )

    ### LEADS

    #for index in range(1, random.randrange(150, 999)):
    #    
    #  start_date = fake.date()
    #  end_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=30)
    #  region = Regions.objects.order_by('?').first().id
    #  provinces = Provinces.objects.filter(region_id=region)      
    #  if len(provinces) > 0:
    #  
    #    province = provinces[random.randrange(0,len(provinces)-1)].id
    #
    #    Leads.objects.create(
    #      title=fake.paragraph(nb_sentences=1),
    #      description=fake.paragraph(nb_sentences=1)[:50].rsplit(' ', 1)[0]+"'...'",
    #      vertical_id=Verticals.objects.order_by('?').first().id,
    #      first_name=fake.first_name(),
    #      last_name=fake.last_name(),
    #      company=fake.company(),
    #      address=fake.street_address(),
    #      region_id=region,
    #      province_id=province,
    #      phone=fake.phone_number() ,
    #      cellular=fake.phone_number() ,
    #      email=fake.ascii_free_email(),
    #      whatsapp=fake.phone_number(),
    #      note=fake.paragraph(nb_sentences=3),
    #      reserved_as_exclusive=random.choice([True, False]),
    #      owner_id=Registry.objects.order_by('?').first().id,
    #      price= float(decimal.Decimal(random.randrange(10,50))/100),
    #      start_date=start_date,
    #      end_date=end_date,
    #      active=True,
    #      deleted=False,
    #    )

    #Take randomly 1/10 of Verticals and insert a special offer with a price random in range 0.99 to 5.10

    ### SPECIAL OFFERS  

    #leads = Leads.objects.filter(active=True, deleted=False)
    #    
    #for offer in range(0, int(len(leads)-1)):
    #
    #  index = random.randint(0,len(leads)-1)
    #  start_interval = random.randint(4,6) * -1
    #  end_interval_past = random.randint(2,3) * -1
    #  end_interval= random.randint(2,5)
    #  start_date = date.today() + relativedelta(months=start_interval)
    #  
    #  if bool(random.getrandbits(1)):
    #  
    #    end_date = date.today() + relativedelta(months=end_interval)
    #
    #  else:
    #
    #    end_date = date.today() + relativedelta(months=end_interval_past)
    #
    #  special_offer = SpecialOffers.objects.create(
    #    lead_id =  leads[index].id,
    #    price = fake.pydecimal(positive=True,min_value=15,max_value=50),
    #    start_date = start_date, 
    #    end_date = end_date,
    #    active = True,
    #    deleted = False
    #  )

# For each Customer generate a random number of rows in range 0 to 20 contains orders with a date random in interval 09-2023 and 12-2023

    #statuses = ('cnt','ann','con','rim')
    #for customer in Registry.objects.all():
    #
    #  for index in range(0, random.randrange(0,20)):
    # 
    #    date = f"2023-{random.randint(9,12):02d}-{random.randint(1,30):02d}"
    #    lead = Leads.objects.all()[random.randint(0, Leads.objects.count() -1)]
    #
    #    order = Orders.objects.create(
    #      registry_id = customer.id,
    #      order = lead.title,
    #      vertical_id = lead.vertical.id,
    #      lead_id = lead.id,
    #      status = statuses[random.randint(0,len(statuses)-1)],
    #      replaced_by = None, 
    #      status_date = date,
    #      creation_date = date,
    #      deleted = False,
    #    )
    #  
    #    print(f"order date {order.creation_date}")

# for each lead generate a random number of sobscribers in range 0 to 5

    #for lead in Leads.objects.all():
    #
    #  for index in range(0, random.randint(0,6)):
    #
    #    lead.subscribers.add(Registry.objects.all()[random.randint(0, Registry.objects.count() -1)])
        
# update vectors inserting random spacal fields

"""
questions = [
  {  
    "question": "Tipo di utilizzo: ",
    "type": "checkbox",
    "answers": [
      {
        "answer": "acqua calda sanitaria",
        "price_modifier": 0
      },
      {
        "answer": "acqua calda e riscaldamento",
        "price_modifier": 0
      }
    ]
  },
  {
    "question": "Consumo annuale in KWh: il mio consumo è di ",
    "type": "radio",
    "answers": [
      {
        "answer": "3.000 kwh/anno (normale utenza domestica)",
        "price_modifier": 0,
      },
      {
        "answer": "3.001 ai 6.000 kwh/anno",
        "price_modifier": 0,
      },
      {
        "answer": "6.001 ai 10.000 kwh/anno",
        "price_modifier": 0,
      },
      {
        "answer": "10.001 ai 20.000 kwh/anno",
        "price_modifier": 0,
      },
      {
        "answer": "20.001 ai 40.000 kwh/anno",
        "price_modifier": 0,
      },
      {
        "answer": "40.000 kwh/anno",
        "price_modifier": 0,
      }
    ]
  },
  {
    "question": "Spesa mensile in elettricità:￼",
    "type": "radio",
    "answers": [
      {
        "answer": "meno di 1000€ mese",
        "price_modifier": -5,
      },
      {
        "answer": "tra 1.000€ e 3.000€ ",
        "price_modifier": 0,
      },
      {
        "answer": "tra 3.000€ e 5.000€ mese ",
        "price_modifier": 1,
      },
      {
        "answer": "tra 5.000€ e 10.000€ mese ",
        "price_modifier": 3,
      },
      {
        "answer": "più di 10.000€ mese ",
        "price_modifier": 5,
      }
    ]
  },
  {
    "question": "Presenza di amianto sul tetto:￼",
    "type": "radio",
    "answers": [
      {
        "answer": "Si",
        "price_modifier": 5,
      },
      {
        "answer": "No",
        "price_modifier": 0,
      }
    ]
  },
  {
    "question": "Tempistica indicativa per l'installazione:￼",
    "type": "radio",
    "answers": [
      {
        "answer": "0 - 1 mese ",
        "price_modifier": 10,
      },
      {
        "answer": "1 - 3 mesi",
        "price_modifier": 5,
      },
      {
        "answer": "3 - 6 mesi ",
        "price_modifier": 0,
      },
      {
        "answer": "oltre 6 mesi",
        "price_modifier": -5,
      }
    ]
  },
  {
    "question": "Finanziamento dell'impianto: ",
    "type": "radio",
    "answers": [
      {
        "answer": "risorse proprie",
        "price_modifier": 10,
      },
      {
        "answer": "risorse proprie",
        "price_modifier": 0,
      }
    ]
  },
  {
    "question": "Tipologia di impianto:￼ ",
    "type": "radio",
    "answers": [
      {
        "answer": "per il riscaldamento, il raffrescamento e per acqua calda",
        "price_modifier": 0,
      },
      {
        "answer": "per il riscaldamento e raffreddamento ad aria con split",
        "price_modifier": 0,
      }
    ]
  }
]

for vertical in Verticals.objects.all():

  special_fields = []  
  
  for index in range(random.randint(0,3)):

    field = questions[random.randint(0,len(questions)-1)]
    special_fields.append(field)
  
  vertical.special_fields = json.dumps(special_fields)
  vertical.save()
  print(f" special_fields {vertical.special_fields}\n\n")
"""
  



"""

  special_fields = []
  
  
    special_field = questions[random.randint(0,len(questions)-1)]
    
    if special_field:
    
      special_fields = special_fields.append(special_field)
  
  print(f"special_fields {type(special_fields)}")
  print(f"special_fields {special_fields}")
  
  
  #  vertical.special_fields = json.dumps(special_fields)


  #  print(f"special_fields {json.dumps(list(special_fields))}")
  
  #vertical.special_fields = '[{'+special_fields[1:-1]+'}]'
  
  vertical.save()
"""


# for lead in Leads.objects.all():
# 
#   lead.price_modifier = random.randint(-10,10)
#   lead.save()
#   
#   print(f" price_modifier {lead.id}: {lead.price_modifier}\n\n")


### verticals_interest_registry

# for vertical in Verticals.objects.all():
# 
#   max_monthly_requests = random.randint(20,100)
#   max_daily_requests = random.randint(2,10)
#   subscribed = bool(random.getrandbits(1))
#   registry = Registry.objects.order_by('?').first()
#   vertical_interest = VerticalsInterest.objects.create(registry=registry, details="",max_monthly_requests=max_monthly_requests,max_daily_requests=max_daily_requests,answers_details='{}',subscribed=subscribed,active=True,deleted=False)
#   
#   for row in range(random.randint(1,5)):
#   
#     vertical_interest.verticals.add(Verticals.objects.order_by('?').first())
#   
#   for row in range(random.randint(1,3)):
#   
#     vertical_interest.geographic_areas.add(Areas.objects.order_by('?').first())

# for offer in SpecialOffers.objects.all():
#  start_interval = random.randint(4,6) * -1
#  end_interval_past = random.randint(2,3) * -1
#  end_interval= random.randint(2,5)
#  offer.start_date = date.today() + relativedelta(months=start_interval)
# 
#  if bool(random.getrandbits(1)):
# 
#    offer.end_date = date.today() + relativedelta(months=end_interval)
# 
#  else:
# 
#    offer.end_date = date.today() + relativedelta(months=end_interval_past)
# 
#  offer.save()
