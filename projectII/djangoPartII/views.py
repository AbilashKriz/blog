from django.shortcuts import render
from django.http import HttpResponse
from djangoPartII.models import AccessRecord, Topic, webpage, Friends
from djangoPartII import forms
from djangoPartII.forms import NewUser

# Create your views here.

def index(request):
    return render(request, 'djangoPartII/index.html')

def help(request):
    return render(request, 'djangoPartII/help.html')

def research(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'djangoPartII/research.html', context=date_dict)

def friends(request):
    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error buddy!")
    return render(request, 'djangoPartII/friends.html', {'form':form})

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


        
    return render(request, 'djangoPartII/form.html', {'form': form})