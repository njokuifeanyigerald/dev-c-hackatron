from django.shortcuts import render
from .form import HomeForm
from .models import Pyladies,DscFuto,DevcHackatron
# Create your views here.
def home(request):
    form = HomeForm()
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            # if form.event == "py":
                Pyladies.objects.create(**form.cleaned_data)
            DscFuto.objects.create(**form.cleaned_data)
            DevcHackatron.objects.create(**form.cleaned_data)
            form  = HomeForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)