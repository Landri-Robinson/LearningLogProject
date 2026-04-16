import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup

from Mainapp.models import Topic, Entry

topics = Topic.objects.all()

for t in topics:
    print(t.id, t.text, t.date_added)


t = Topic.objects.get(id=1)

print(t)
print(t.date_added)

entries = Entry.objects.filter(topic=t)

for entry in entries:
    print(entry)