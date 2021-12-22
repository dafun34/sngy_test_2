from django.contrib import admin

from .models import Occupation

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'company_name',
                    'position_name')


admin.site.register(Occupation, OccupationAdmin)