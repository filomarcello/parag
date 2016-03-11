from django.contrib import admin

from parag.admin import centersadmin
from patients.models import Patient

class StaffAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Anagrafica',  {'fields': ['centro', 'cognome', 'nome', 'sesso',
                                    'd_nascita', 'eta_diagnosi', 'dna',
                                    'd_dna']}),

        ('Anamnesi',    {'fields': ['famigliarita', 'note_famigliarita',
                                    'comorbidita', 'note_comorbidita',
                                    'anamnesi_chirurgica',]}),

        ('Ematochimici', {'fields': ['cga', 'nau', 'dau', 'mnu', 'nmu',
                                     'diuresi',]}),

        ('Paraganglioma', {'fields': ['sede', 'lateralita', 'dim_x', 'dim_y',
                                      'dim_z', 'sede_note',]}),

        ('Imaging',     {'fields': ['d_imaging', 'referto_imaging',
                                    'd_recettoriale', 'referto_recettoriale',
                                    'd_dopa', 'referto_dopa',]}),

        ('Intervento',  {'fields': ['d_intervento', 'tipo', 'accesso',
                                    'embolizzazione', 'procedure',
                                    'complicanze_intra', 'note_complicanze_intra',
                                    'complicanze_post', 'note_complicanze_post',
                                    ]}),

        ('Istologico',  {'fields': ['referto_isto', 'malignita', 'ki67', 'iic',
                                    ]}),

        ('Follow up',   {'fields': ['metastasi', 'note_metastasi', 'recidiva',
                                    'note_recidiva', 'nuove_loca',
                                    'note_nuove_loca',]}),

        ('Genetica',            {'fields': ['mat_genetico', 'sdha',
                                            'sdha_risultati', 'sdha_tipo',
                                           'sdhaf2', 'sdhaf2_risultati',
                                            'sdhaf2_tipo',
                                           'sdhb', 'sdhb_risultati', 'sdhb_tipo',
                                           'sdhc', 'sdhc_risultati', 'sdhc_tipo',
                                           'sdhd', 'sdhd_risultati', 'sdhd_tipo',
                                           'genetica_note',]}),
    ]

    list_filter = ['d_nascita',]

    search_fields = ['cognome', 'd_nascita',]
    list_display = ('cognome', 'nome', 'sesso', 'd_nascita')


class CentersAdmin(admin.ModelAdmin):

    search_fields = ['cognome', 'd_nascita',]
    list_display = ('cognome', 'nome', 'sesso',)

    fieldsets = [
        ('Anagrafica',  {'fields': ['centro', 'cognome', 'nome', 'sesso',
                                    'd_nascita', 'eta_diagnosi', 'dna',
                                    'd_dna']}),

        ('Anamnesi',    {'fields': ['famigliarita', 'note_famigliarita',
                                    'comorbidita', 'note_comorbidita',
                                    'anamnesi_chirurgica',]}),

        ('Ematochimici', {'fields': ['cga', 'nau', 'dau', 'mnu', 'nmu',
                                     'diuresi',]}),

        ('Paraganglioma', {'fields': ['sede', 'lateralita', 'dim_x', 'dim_y',
                                      'dim_z', 'sede_note',]}),

        ('Imaging',     {'fields': ['d_imaging', 'referto_imaging',
                                    'd_recettoriale', 'referto_recettoriale',
                                    'd_dopa', 'referto_dopa',]}),

        ('Intervento',  {'fields': ['d_intervento', 'tipo', 'accesso',
                                    'embolizzazione', 'procedure',
                                    'complicanze_intra', 'note_complicanze_intra',
                                    'complicanze_post', 'note_complicanze_post',
                                    ]}),

        ('Istologico',  {'fields': ['referto_isto', 'malignita', 'ki67', 'iic',
                                    ]}),

        ('Follow up',   {'fields': ['metastasi', 'note_metastasi', 'recidiva',
                                    'note_recidiva', 'nuove_loca',
                                    'note_nuove_loca',]}),
    ]

    exclude = ('mat_genetico', 'sdha', 'sdha_risultati', 'sdha_tipo',
               'sdhaf2', 'sdhaf2_risultati', 'sdhaf2_tipo',
               'sdhb', 'sdhb_risultati', 'sdhb_tipo',
               'sdhc', 'sdhc_risultati', 'sdhc_tipo',
               'sdhd', 'sdhd_risultati', 'sdhd_tipo',
               'genetica_note',)


admin.site.register(Patient, StaffAdmin)
centersadmin.register(Patient, CentersAdmin)