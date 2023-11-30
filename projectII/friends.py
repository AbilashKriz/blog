import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectII.settings')

import django

django.setup()

import random
from djangoPartII.models import Friends
from faker import Faker

fakegen = Faker()

def populate(n):
    for entry in range(n):
        fake_first = fakegen.name()
        fake_last = fakegen.name()
        fake_email = fakegen.email()
    

        friends = Friends.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_email )[0]
    

if __name__ == '__main__':
    print("Populating script!!")
    populate(20)
    
    print("Populating completed!")
