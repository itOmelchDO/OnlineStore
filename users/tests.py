from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse("users:registration")

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "DESIREX Store - Реєстрація")
        self.assertTemplateUsed(response, "users/registration.html")
