from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Group


class GroupList(ListView):
    model = Group
    template_name = 'group-list.html'


class GroupCreate(CreateView):
    model = Group
    template_name = 'group-form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('groups-list')


class GroupUpdate(UpdateView):
    model = Group
    template_name = 'group-form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('groups-list')


class GroupDelete(DeleteView):
    model = Group
    template_name = 'group-confirm-delete.html'
    success_url = reverse_lazy('groups-list')
    