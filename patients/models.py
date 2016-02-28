# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

DATE_HELP = "N.B. Inserire la data nel formato <b>GG-MM-AAAA</b>"
DNA_HELP = "Cliccare se al paziente è già stato prelevato il DNA \
(due provette emocromo da conservare a -20°C)"
OBBLIGATORIO = " Campo obbligatorio"

class Patient(models.Model):

    class Meta:
        verbose_name_plural = 'Pazienti'

    def __str__(self):
        return ' '.join((self.cognome, self.nome, self.d_nascita))

    centro = models.CharField(max_length=100)

    # anagrafica

    cognome = models.CharField(max_length=50,
                               verbose_name="Cognome del paziente",
                               help_text=OBBLIGATORIO)

    nome = models.CharField(max_length=50,
                            verbose_name="Nome del paziente",
                            help_text=OBBLIGATORIO)

    sesso = models.CharField(max_length=1,
                             choices=(('M', 'maschio'),
                                      ('F', 'femmina')),
                                      help_text=OBBLIGATORIO)

    d_nascita = models.DateField(verbose_name="Data di nascita",
                                 help_text=DATE_HELP+OBBLIGATORIO)

    eta_diagnosi = models.IntegerField(verbose_name="Età alla diagnosi",
                                      help_text="In anni"+OBBLIGATORIO)

    dna = models.BooleanField(verbose_name="Prelevato DNA",
                              help_text=DNA_HELP)

    d_dna = models.DateField(verbose_name="Data del prelievo di DNA",
                             help_text=DATE_HELP,
                             blank=True,
                             null=True)

    # anamnesi

    famigliarita = models.BooleanField(
        verbose_name="Famigliarità per paragangliomi")

    note_famigliarita = models.TextField(
        verbose_name='Dettagli riguardanti la famigliarità',
                                         blank=True,
                                         null=True)

    comorbidita = models.CharField(max_length=25,
                                   verbose_name="Comorbidità",
                                   choices=(('ignote', "Non indagate"),
                                            ('no', 'nessuna'),
                                            ('gist', 'GIST'),
                                            ('ca_tiroide', "Carcinoma tiroideo"),
                                            ('ad_surrene', "Adenoma surrenalico"),
                                            ('feo', 'Feocromocitoma')),
                                    blank=True,
                                    null=True)

    note_comorbidita = models.TextField(
        verbose_name="Altre comorbidità eventualmente presenti",
                                        blank=True,
                                        null=True)

    anamnesi_chirurgica = models.TextField(
        verbose_name="Interventi chirurgici effettuati",
        blank=True,
        null=True,
        help_text="N.B. mettere qui un eventuale intervento pregresso sul \
        paraganglioma in questione")

    # ematochimici

    cga = models.FloatField(verbose_name="Cromogranina A",
                            blank=True,
                            null=True) # TODO unità di misura

    nau = models.FloatField(verbose_name="Noradrenalina urinaria",
                            blank=True,
                            null=True) # TODO unità di misura

    dau = models.FloatField(verbose_name="Dopamina urinaria",
                            blank=True,
                            null=True) # TODO unità di misura

    mnu = models.FloatField(verbose_name="Metanefrina urinaria",
                            blank=True,
                            null=True) # TODO unità di misura

    nmu = models.FloatField(verbose_name="Normetanefrina urinaria",
                            blank=True,
                            null=True) # TODO unità di misura

    diuresi = models.IntegerField(verbose_name="Diuresi",
                                  help_text="In cc o ml",
                                  blank=True,
                                  null=True)

    # paraganglioma

    sede = models.CharField(max_length=100,
        verbose_name="Sede del paraganglioma",
        choices=(('collo', 'collo'),
                 ('torace', 'torace'),
                 ('addome', 'addome'),
                 ('timpanico', 'timpanico (A)'),
                 ('timpmast', 'timpano-mastoideo (B)'),
                 ('giugulare', 'giugulare (C)'),
                 ('giugintraextra', 'giugulare-intracranica extradurale (De)'),
                 ('giugintraintra', 'giugulare-intracranica intradurale (Di)'),),
                 help_text=OBBLIGATORIO)

    lateralita = models.CharField(max_length=10,
                                  verbose_name="lateralità",
                                  choices=(('ds', 'destra'),
                                           ('sn', 'sinistra'),
                                           ('bilat', 'bilaterale'),
                                           ('na', 'N/A'),),
                                  help_text=OBBLIGATORIO)

    dim_x = models.IntegerField(verbose_name="Diametro 1",
                                help_text="In millimetri"+OBBLIGATORIO)

    dim_y = models.IntegerField(verbose_name="Diametro 2",
                                help_text="In millimetri",
                                blank=True,
                                null=True)

    dim_z = models.IntegerField(verbose_name="Diametro 3",
                                help_text="In millimetri",
                                blank=True,
                                null=True)

    sede_note = models.TextField(verbose_name="Eventuali dettagli riguardanti la sede del paraganglioma",
                                 blank=True,
                                 null=True)

    # imaging

    d_imaging = models.DateField(verbose_name="Data dell'imaging anatomico",
                            help_text="(p.es. RMN, TAC, ecografia) "+DATE_HELP,
                            blank=True,
                            null=True)

    referto_imaging = models.TextField(
        verbose_name="Referto dell'imaging anatomico",
           help_text="Specificare anche il tipo di imaging",
           blank=True,
           null=True)

    d_recettoriale = models.DateField(
        verbose_name="Data dell'imaging recettoriale",
          help_text=DATE_HELP,
          blank=True,
          null=True)

    referto_recettoriale = models.TextField(
        verbose_name="Referto dell'imaging recettoriale",
            help_text="Specificare anche il tipo di tracciante",
            blank=True,
            null=True)

    # dopa

    d_dopa = models.DateField(verbose_name="Data della DOPA",
                              help_text=DATE_HELP,
                              blank=True,
                              null= True)

    referto_dopa = models.TextField(verbose_name="Referto della DOPA",
                                    blank=True,
                                    null=True)

    # intervento

    d_intervento = models.DateField(
        verbose_name="Data dell'intervento chirurgico",
                            help_text=DATE_HELP,
                            blank=True,
                            null=True)

    tipo = models.CharField(max_length=20,
                            choices=(('asportazione', 'asportazione'),
                                     ('debulking', 'debulking'),),
                            verbose_name="Tipo di intervento",
                            blank=True,
                            null=True)

    accesso = models.CharField(max_length=50,
                               choices=(('cervicotomia', 'cervicotomia'),
                                        ('laparoscopia', 'laparoscopia'),
                                        ('laparotomia', 'laparotomia'),
                                        ('transmeatale', 'transmeatale'),
                                        ('transmasto', 'transmastoidea'),
                                        ('infratemp', 'infratemporale'),),
                               verbose_name="Accesso chirurgico",
                               blank=True,
                               null=True)

    embolizzazione = models.BooleanField(
        verbose_name="Embolizzazione preoperatoria")


    procedure = models.TextField(verbose_name="Procedure associate",
                                 blank=True,
                                 null=True)

    complicanze_intra = models.CharField(
        verbose_name="Complicanze intraoperatorie",
             choices=(('legatura', "Legatura vascolare per emorragia"),
                      ('res_nervo', "Resezione nervo"),
                      ('no', 'Nessuna')),
             max_length=20,
             blank=True,
             null=True)

    note_complicanze_intra = models.TextField(
        verbose_name="Complicanze intraoperatorie: note",
         blank=True,
         null=True,
         help_text="Dettagli sulle eventuali complicanze intraoperatorie avvenute")

    complicanze_post = models.CharField(max_length=20,
        choices=(('les_nervo', "Lesione nervo"),
                 ('ematoma', 'Ematoma'),
                 ('no', 'Nessuna')),
        verbose_name="Complicanze post-operatorie",
        blank=True,
        null=True)

    note_complicanze_post = models.TextField(
        verbose_name="Dettagli sulle eventuali complicanze post-operatorie avvenute",
             blank=True,
             null=True)

# istologico

    referto_isto = models.TextField(verbose_name="Referto istologico",
                                    blank=True,
                                    null=True)

    malignita = models.BooleanField(verbose_name="Malignità istologica")

    ki67 = models.IntegerField(
        verbose_name="Indice di proliferazione cellulare (Mib1/Ki67)",
               help_text="Percentuale (N.B. non aggiungere il carattere '%')",
               blank=True,
               null=True)

    iic = models.TextField(verbose_name="Immunoistochimica",
                   help_text="Eventuale esame immunoistochimico disponibile",
                   blank=True,
                   null=True)

    # follow up

    metastasi = models.CharField(max_length=20,
                                 verbose_name="Presenza di metastasi",
                                 choices=(('linfonodi', 'Linfonodali'),
                                          ('distanza', "A distanza"),
                                          ('no', 'Nessuna')),
                                 blank=True,
                                 null=True)

    note_metastasi = models.TextField(verbose_name="Dettagli metastasi",
                                      help_text="Specificare sede e caratteristiche di eventuali metastasi",
                                      blank=True,
                                      null=True)

    recidiva = models.BooleanField(verbose_name="Recidiva locoregionale",
           help_text="Cliccare se presente recidiva locoregionale nel follow up")

    note_recidiva = models.TextField(
        verbose_name="Dettagli recidiva locoregionale",
         help_text="Specificare i dettagli di eventuale recidiva locoregionale",
         blank=True,
         null=True)

    nuove_loca = models.BooleanField(verbose_name="Nuove localizzazioni",
         help_text="Cliccare se presenti nuove localizzazioni di paragangliomi \
         nel follow up")

    note_nuove_loca = models.TextField(
        verbose_name="Dettagli nuove localizzazioni",
           help_text="Specificare la sede e i dettagli di eventuale nuove \
           localizzazioni di paragangliomi",
           blank=True,
           null=True)

# genetica

    mat_genetico = models.CharField(verbose_name="Materiale genetico",
                        help_text="Materiale genetico esaminato",
                        max_length=15,
                        choices=(('dna_periferico', 'DNA da sangue periferico'),
                                 ('dna_buccale', 'DNA da tampone buccale'),
                                 ('dna_tumorale', 'DNA da tessuto tumorale'),
                                 ('rna_periferico', 'RNA da sangue periferico'),
                                 ('rna_tumorale', 'RNA da tessuto tumorale'),
                                 ('altro', 'altro'),),
                        blank=True,
                        null=True)

    sdha = models.BooleanField(verbose_name="Gene SDHA",
                           help_text="Selezionare se esaminato il gene SDHA")

    sdha_risultati = models.TextField(verbose_name="Risultati gene SDHA",
                                      blank=True,
                                      null=True)

    sdha_tipo = models.CharField(verbose_name="Tipologia dei risultati gene SDHA",
             max_length=25,
             choices=(('varianti_pat', "Varianti patogenetiche"),
                      ('varianti_incerto', "Varianti ad incerto significato"),
                      ('polimorfismi', 'Polimorfismi')),
             blank=True,
             null=True)

    sdhaf2 = models.BooleanField(verbose_name="Gene SDHAF2",
                           help_text="Selezionare se esaminato il gene SDHAF2")

    sdhaf2_risultati = models.TextField(verbose_name="Risultati gene SDHAF2",
                                      blank=True,
                                      null=True)

    sdhaf2_tipo = models.CharField(verbose_name="Tipologia dei risultati gene SDHAF2",
             max_length=25,
             choices=(('varianti_pat', "Varianti patogenetiche"),
                      ('varianti_incerto', "Varianti ad incerto significato"),
                      ('polimorfismi', 'Polimorfismi')),
             blank=True,
             null=True)

    sdhb = models.BooleanField(verbose_name="Gene SDHB",
                           help_text="Selezionare se esaminato il gene SDHB")

    sdhb_risultati = models.TextField(verbose_name="Risultati gene SDHB",
                                      blank=True,
                                      null=True)

    sdhb_tipo = models.CharField(verbose_name="Tipologia dei risultati gene SDHB",
             max_length=25,
             choices=(('varianti_pat', "Varianti patogenetiche"),
                      ('varianti_incerto', "Varianti ad incerto significato"),
                      ('polimorfismi', 'Polimorfismi')),
             blank=True,
             null=True)

    sdhc = models.BooleanField(verbose_name="Gene SDHC",
                           help_text="Selezionare se esaminato il gene SDHC")

    sdhc_risultati = models.TextField(verbose_name="Risultati gene SDHC",
                              blank=True,
                              null=True)

    sdhc_tipo = models.CharField(verbose_name="Tipologia dei risultati gene SDHC",
             max_length=25,
             choices=(('varianti_pat', "Varianti patogenetiche"),
                      ('varianti_incerto', "Varianti ad incerto significato"),
                      ('polimorfismi', 'Polimorfismi')),
             blank=True,
             null=True)

    sdhd = models.BooleanField(verbose_name="Gene SDHD",
                       help_text="Selezionare se esaminato il gene SDHD")

    sdhd_risultati = models.TextField(verbose_name="Risultati gene SDHD",
                                      blank=True,
                                      null=True)

    sdhd_tipo = models.CharField(verbose_name="Tipologia dei risultati gene SDHD",
             max_length=25,
             choices=(('varianti_pat', "Varianti patogenetiche"),
                      ('varianti_incerto', "Varianti ad incerto significato"),
                      ('polimorfismi', 'Polimorfismi')),
             blank=True,
             null=True)

    genetica_note = models.TextField(verbose_name="Commento",
                     help_text="Note sul quadro genetico del paziente",
                     blank=True,
                     null=True)




