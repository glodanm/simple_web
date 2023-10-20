from django.urls import path
from .views import UserList, UserCreate, UserUpdate, UserDelete


urlpatterns = [
    path('', UserList.as_view(), name='users-list'),
    path('add/', UserCreate.as_view(), name='user-add'),
    path('edit/<int:pk>/', UserUpdate.as_view(), name='user-edit'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='user-delete'),
]
