from django.contrib import admin
from frontend.models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(SubscribeModel)
admin.site.register(Contact)
admin.site.site_header = 'Allinone'
