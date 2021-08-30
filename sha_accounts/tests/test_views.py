from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from djrest_wrapper.exceptions.apis import errors


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_user_view(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'test'
        }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('err'), False)
        self.assertEqual(response.json().get(
            'err_code'), errors.ERR_SUCCESSFUL)
        self.assertIsNotNone(response.json().get('data').get('user').get('access_token'))
    
    def test_signin_user_view(self):
        self.test_create_user_view()
        url = reverse('user-signin')
        data = {
            'username': 'testuser',
            'password': 'test'
        }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.json().get('err'),False)
        self.assertEqual(response.json().get('err_code'),errors.ERR_SUCCESSFUL)
        self.assertIsNotNone(response.json().get('data').get('user').get('access_token'))