from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Collar
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .forms import TrainerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    collars_not_owned = Collar.objects.exclude(id__in = dog.collars.all().values_list('id'))
    trainer_form = TrainerForm()
    return render(request, 'dogs/detail.html', {'dog':dog, 'trainer_form': trainer_form, 'collars':collars_not_owned})

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'weight']

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description','weight']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

def add_trainer(request, dog_id):
    form = TrainerForm(request.POST)
    if form.is_valid():
        new_trainer = form.save(commit=False)
        new_trainer.dog_id = dog_id
        new_trainer.save()
    return redirect('detail', dog_id=dog_id)

def assoc_collar(request, dog_id, collar_id):
    Dog.objects.get(id=dog_id).collars.add(collar_id)
    return redirect('detail', dog_id=dog_id)

def unassoc_collar(request, dog_id, collar_id):
    Dog.objects.get(id= dog_id).collars.remove(collar_id)
    return redirect('detail', dog_id=dog_id)

