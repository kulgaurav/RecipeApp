from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_mail(self):
        """Test creating a new user"""
        email = "test@kul.com"
        password = "asd123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@KUL.com"
        user = get_user_model().objects.create_user(email, "")

        self.assertEqual(user.email, email.lower())
