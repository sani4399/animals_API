from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpass")

    def test_user_created(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")
