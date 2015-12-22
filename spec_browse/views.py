from django.shortcuts import render,redirect, get_object_or_404
from spec_browse.models import Molecules
from django.core import serializers

# Create your views here.
def home_page(request):
    mols = Molecules.objects.all()
    return render(request,'spec_browse/mol_list.html', {"mols": mols,"mol_count":mols.count()})

def mol_detail(request,pk):
    mol = get_object_or_404(Molecules, pk=pk)
    return render(request, 'spec_browse/mol_detail.html', {'mol': mol})