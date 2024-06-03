from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Card

class CardAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_create_card_valid(self):
    
        data = {
        'title': 'Test Card',
        'card_number': '1234123412341234',
        'ccv': '123'
    }
        response = self.client.post('/api/cards/', data)
        print(response.data)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_card_invalid_data(self):
        data = {'title': 'Invalid Card', 'card_number': '1234', 'ccv': '12'}
        response = self.client.post('/api/cards/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_performance(self):
        import time
        start_time = time.time()
        for _ in range(100):
            card_number = '1234123412341234'  
            ccv = '123'
            self.client.post('/api/cards/', {'title': 'Perf Card', 'card_number': card_number, 'ccv': ccv})
            end_time = time.time()
        self.assertLess(end_time - start_time, 10)  



