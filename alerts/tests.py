from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Alert

class AlertAPITestCase(APITestCase):

    def setUp(self):
        # 1. Create test users
        self.user_a = User.objects.create_user(username='testusera', password='testapassword')
        self.user_b = User.objects.create_user(username='testuserb', password='testbpassword')
        self.url = '/api/alerts/'

    def test_create_alert(self):
        # Authenticate specifically as User A for this test
        self.client.force_authenticate(user=self.user_a)

        # Do not include 'user' in payload; perform_create handles this in views.py
        data = {
            'symbol': 'EURUSD',
            'target_price': '1.1050',
            'condition': 'ABOVE',
            'is_active': True
        }

        response = self.client.post(self.url, data, format='json')
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 1)
        
        # Verify the created alert belongs to User A
        alert = Alert.objects.get()
        self.assertEqual(alert.symbol, 'EURUSD')
        self.assertEqual(alert.user, self.user_a)

    def test_get_alerts_returns_only_user_owned_alerts(self):
        # Seed test database with alerts for both users
        Alert.objects.create(user=self.user_a, symbol='EURUSD', target_price=1.1050, condition='ABOVE', is_active=True)
        Alert.objects.create(user=self.user_b, symbol='GBPUSD', target_price=1.34567, condition='BELOW', is_active=True)

        # Authenticate as User A
        self.client.force_authenticate(user=self.user_a)

        response = self.client.get(self.url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # User A should ONLY see 1 alert (their own), not User B's alert
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], 'EURUSD')