from django.contrib import admin

# Register your models here.
from .models import Etudiant, Cours, Absence

admin.site.register(Etudiant)
admin.site.register(Cours)
admin.site.register(Absence)