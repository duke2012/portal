from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Atmb)
admin.site.register(Lightning_Receptor)
admin.site.register(Down_Lead_Line)
admin.site.register(Earth_Device)
admin.site.register(Thunder_External_Protect)
admin.site.register(Power_SPD)