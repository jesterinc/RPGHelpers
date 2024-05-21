from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.conf import settings

from commons.models import *
from meetings.models import *
from direct_sales.models import *

from faker import Faker
import random
from random import randint

class Command(BaseCommand):
  help = 'Filler of DB'

  def handle(self, *args, **options):

    faker = Faker(['it_IT'])

    for category in range(0,10):

      offer_category = OffersCategories(name=faker.word())
      offer_category.save()

    offer_categories = OffersCategories.objects.all()

    for offer in Offers.objects.all():

      offer.offer_category_id = offer_categories[randint(0,len(offer_categories)-1)]
      offer.save()

    for category in range(0,10):

      kit_category = KitsCategories(name=faker.word())
      kit_category.save()

    kit_categories = KitsCategories.objects.all()

    for kit in Kits.objects.all():

      kit.kit_category_id = kit_categories[randint(0,len(kit_categories)-1)]
      kit.save()

