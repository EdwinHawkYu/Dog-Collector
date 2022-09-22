from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Collar
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .forms import TrainerForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    collars_not_owned = Collar.objects.exclude(id__in = dog.collars.all().values_list('id'))
    trainer_form = TrainerForm()
    return render(request, 'dogs/detail.html', {'dog':dog, 'trainer_form': trainer_form, 'collars':collars_not_owned})

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'weight']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['breed', 'description','weight']

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'

@login_required
def add_trainer(request, dog_id):
    form = TrainerForm(request.POST)
    if form.is_valid():
        new_trainer = form.save(commit=False)
        new_trainer.dog_id = dog_id
        new_trainer.save()
    return redirect('detail', dog_id=dog_id)

@login_required
def assoc_collar(request, dog_id, collar_id):
    Dog.objects.get(id=dog_id).collars.add(collar_id)
    return redirect('detail', dog_id=dog_id)

@login_required
def unassoc_collar(request, dog_id, collar_id):
    Dog.objects.get(id= dog_id).collars.remove(collar_id)
    return redirect('detail', dog_id=dog_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

