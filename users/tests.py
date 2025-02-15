from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = "Test User",
            email = "test@mail.com",
            password = "test@123"
        )
    def test_user_creation(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.is_superuser,False)
        self.assertEqual(user.is_staff,False)
        self.assertEqual(user.username,"Test User")