from django.shortcuts import render, redirect
from .forms import EtudiantForm

def inscrire_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/inscription.html', {'form': form})