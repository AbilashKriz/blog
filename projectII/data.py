#!/path/to/your/virtual/environment/python
import os
import sys

# Correct the typo in the environment variable name
# sys.path.append(os.path.join(os.path.dirname(__file__), 'projectII'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectII.settings')
import django

django.setup()

# Make sure the settings are configured before accessing them


import random
from djangoPartII.models import AccessRecord, webpage, Topic

from faker import Faker

fakegen = Faker()

topics = ['search', 'Social', 'Marketplace', 'News', 'Game']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!!")
    populate(20)
    print("Populating completed!")
