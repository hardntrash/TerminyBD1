from django.shortcuts import render
from django import forms
from django.utils.datastructures import MultiValueDictKeyError

from .models import TerminyModel


# Create your views here.

class MainForm(forms.ModelForm):
    choose_termin = forms.ModelChoiceField(queryset=TerminyModel.objects.all(),
                                           empty_label="Выбери термин",
                                           widget=forms.Select(attrs={'termin': 'dropdown', 'class': 'dropdown-list'}), label="Термин")

    class Meta:
        model = TerminyModel
        fields = ('termin',)


def IndexView(request):
    try:
        termin = None
        message = None
        terminObj = TerminyModel.objects.filter(id=request.GET['choose_termin']).first()
        if terminObj != None:
            message = terminObj.description
            termin = terminObj.termin
        return render(request, 'index.html', {'form': MainForm, 'termin': termin, 'message': message})
    except MultiValueDictKeyError:
        return render(request, 'index.html', {'form': MainForm})



def ShowTerminView(request):
    message = None
    termin = TerminyModel.objects.filter(id=request.GET['choose_termin']).first()
    if termin != None:
        print('ye')
        message = termin.description
    return render(request, 'index.html', {'message': message})
