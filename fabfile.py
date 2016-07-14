import django
django.setup()
from lum.models import *
def clear():
    Lab.objects.all().delete()
    Author.objects.all().delete()
    Publication.objects.all().delete()