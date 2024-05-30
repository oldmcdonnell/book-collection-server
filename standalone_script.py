import os
import django
from django.conf import settings

# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "project_book.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW
from app_book.models import *

book_data = [
    {'title': 'The Revolt of the Angels', 'author': 'La Carmina', 'genre': 'Fiction'},
    {'title': 'The Little Book of Satanism', 'author': 'Anatole France', 'genre': 'Religion'},
    {'title': 'Outbreak: A Crisis of Faith: How Religion Ruined Our Global Pandemic', 'author': 'Noah lugeons', 'independent': 'Religion'},
]

Books.objects.bulk_create(book_data)

