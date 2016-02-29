from django.contrib import admin
from patients.models import Patient

class StaffAdmin(admin.ModelAdmin):

    # TODO fieldsets for each section of the model
    # fieldsets = [
    #     ('Anagrafica',          {'fields': []}),
    #     ('Genetica',            {'fields': []}),
    # ]

    # list_filter = ['d_nascita',]

    search_fields = ['cognome', 'd_nascita',]

admin.site.register(Patient, StaffAdmin)

# TODO different ModelAdmin for staff and centers
