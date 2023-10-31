from django.contrib import admin
from . models import visitor,securitydata,securityIncident,securityShift
# Register your models here.

admin.site.register(visitor)
admin.site.register(securitydata)
admin.site.register(securityIncident)
admin.site.register(securityShift)



