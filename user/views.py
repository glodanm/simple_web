from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from group.models import Group


class GroupContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class UserList(ListView):
    model = User
    template_name = 'user-list.html'


class UserCreate(GroupContextMixin, CreateView):
    model = User
    template_name = 'user-form.html'
    fields = ['username', 'group']
    success_url = reverse_lazy('users-list')


class UserUpdate(GroupContextMixin, UpdateView):
    model = User
    template_name = 'user-form.html'
    fields = ['username', 'group']
    success_url = reverse_lazy('users-list')


class UserDelete(DeleteView):
    model = User
    template_name = 'user-confirm-delete.html'
    success_url = reverse_lazy('users-list')
