from django.test import TestCase
from django.urls import reverse
from .models import User


class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")

    def test_user_list_view(self):
        response = self.client.get(reverse('users-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-list.html')

    def test_user_create_view(self):
        response = self.client.get(reverse('user-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-form.html')

    def test_user_update_view(self):
        response = self.client.get(reverse('user-edit', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-form.html')

    def test_user_delete_view(self):
        response = self.client.get(reverse('user-delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-confirm-delete.html')
