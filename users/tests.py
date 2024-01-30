from django.test import TestCase

# Create your tests here.

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import serializers



class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_with_valid_data(self):
        payload = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'firstName': 'John',
            'lastName': 'Doe',
            'gender': 'Male',
            'address': '123 Main St',
            'phoneNumber': '+123456789',
        }
        response = self.client.post('/users/register', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_invalid_data(self):
        payload = {
            'email': 'test@example.com',
            'username': '',  # Invalid: Empty username
            'password': 'testpassword',
            'firstName': 'John',
            'lastName': 'Doe',
            'gender': 'Male',
            'address': '123 Main St',
            'phoneNumber': '+123456789',
        }
        response = self.client.post('/users/register', payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Additional assertions based on the expected error response

    # Add more test cases as needed

    def test_register_with_noname(self):
        payload = {
            'email': 'test@example.com',
            'username': 'test',  # Invalid: Empty username
            'password': 'testpassword',
            'firstName': '',
            'lastName': 'Doe',
            'gender': 'Male',
            'address': '123 Main St',
            'phoneNumber': '+123456789',
        }
        response = self.client.post('/users/register', payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Additional assertions based on the expected error response

    # def test_company_user(self):
    #     payload = {
    #         'email': 'company_user@company.com',
    #         'username': 'company_user',  # Invalid: Empty username
    #         'password': 'testpassword',
    #         'firstName': 'John',
    #         'lastName': 'Doe',
    #         'gender': 'Male',
    #         'address': '123 Main St',
    #         'phoneNumber': '+123456789',
    #         'company': 1,
    #         'role':'recruiter'
    #     }
    #     response = self.client.post('/users/register-company', payload)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Additional assertions based on the expected error response