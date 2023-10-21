from django.test import TestCase
from django.urls import reverse
from .models import Group


class GroupViewsTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="Test Group", description="Test Description")

    def test_group_list_view(self):
        response = self.client.get(reverse('groups-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'group-list.html')

    def test_group_create_view(self):
        response = self.client.get(reverse('group-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'group-form.html')

    def test_group_update_view(self):
        response = self.client.get(reverse('group-edit', kwargs={'pk': self.group.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'group-form.html')

    def test_group_delete_view(self):
        response = self.client.get(reverse('group-delete', kwargs={'pk': self.group.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'group-confirm-delete.html')
