import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','repetitor.settings')

import django
# Import settings
django.setup()

import random
from requestApp.models import Student, Course
from faker import Faker

fakegen = Faker()
topics = ['Individual course','Publish course','Solo course','Single course']

def add_topic():
    t = Course.objects.get_or_create(course_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry
        fake_name = fakegen.name().split()[0]
        fake_last_name = fakegen.name().split()[1]
        fake_phone = fakegen.phone_number()
        fake_date_pub = fakegen.date()
        fake_email = fakegen.email()

        # Create new Webpage Entry
        std = Student.objects.get_or_create(courses=top,name=fake_name,
                                              last_name=fake_last_name, phone=fake_phone, date_pub=fake_date_pub, email=fake_email)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        # accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
