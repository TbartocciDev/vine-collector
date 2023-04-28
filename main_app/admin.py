from django.contrib import admin
from .models import Wine, SoldDate

# Register your models here.
admin.site.register(Wine)
admin.site.register(SoldDate)
