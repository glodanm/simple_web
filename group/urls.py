from django.urls import path
from .views import GroupList, GroupCreate, GroupUpdate, GroupDelete

urlpatterns = [
    path('', GroupList.as_view(), name='groups-list'),
    path('add/', GroupCreate.as_view(), name='group-add'),
    path('edit/<int:pk>/', GroupUpdate.as_view(), name='group-edit'),
    path('delete/<int:pk>/', GroupDelete.as_view(), name='group-delete'),
]
