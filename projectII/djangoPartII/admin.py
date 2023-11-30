from django.contrib import admin
from djangoPartII.models import AccessRecord, Topic, webpage, Friends
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(Friends)

