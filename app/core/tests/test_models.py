from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
     def test_create_user_model_with_successful(self):
         """creating new user wth email is successful"""
         email='test@ramkumarmandal.com'
         password='ramkumar'
         user = get_user_model().objects.create_user(
             email=email,
             password=password
         )
         self.assertEqual(user.email, email)
         self.assertTrue(user.check_password(password))