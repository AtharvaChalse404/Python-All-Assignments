''' Cant Add Multiple Files so Added Everthing in one file '''



# models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    language = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# forms.py
from django import forms
from .models import State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'population', 'language', 'capital']



# views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import State
from .forms import StateForm

class StateListView(ListView):
    model = State

class StateDetailView(DetailView):
    model = State

class StateCreateView(CreateView):
    model = State
    form_class = StateForm
    success_url = reverse_lazy('state_list')

class StateUpdateView(UpdateView):
    model = State
    form_class = StateForm
    success_url = reverse_lazy('state_list')

class StateDeleteView(DeleteView):
    model = State
    success_url = reverse_lazy('state_list')



# urls.py
from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state_list'),
    path('state/<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('state/new/', StateCreateView.as_view(), name='state_create'),
    path('state/<int:pk>/update/', StateUpdateView.as_view(), name='state_update'),
    path('state/<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
]



