from django.shortcuts import render

# Create your views here.
from .models import Etudiant, Cours, Absence

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})

def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'liste_cours.html', {'cours': cours})

def enregistrer_absence(request):
    if request.method == 'POST':
        etudiant_id = request.POST.get('etudiant_id')
        cours_id = request.POST.get('cours_id')
        etudiant = Etudiant.objects.get(id=etudiant_id)
        cours = Cours.objects.get(id=cours_id)
        Absence.objects.create(etudiant=etudiant, cours=cours)
        return HttpResponse("Absence enregistrée avec succès.")
    else:
        etudiants = Etudiant.objects.all()
        cours = Cours.objects.all()
        return render(request, 'enregistrer_absence.html', {'etudiants': etudiants, 'cours': cours})


