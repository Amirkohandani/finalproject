from django.test import TestCase
from rest_framework.test import APIClient
from .models import VehicleData
class VehicleDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = VehicleData.objects.create(
        url="http://example.com/car1",
        title="Car 1",
        time="2024-09-04",
        year="2020",
        image="http://example.com/image.jpg",
        mileage="10000",
        location="New York",
        description="A nice car",
        price="20000"
        )

def test_create_vehicle_data(self):
    response = self.client.post('/vehicle_data/', {
    'url': 'http://example.com/car2',
    'title': 'Car 2',
    'time': '2024-09-04',
    'year': '2021',
    'image': 'http://example.com/image2.jpg',
    'mileage': '5000',
    'location': 'Los Angeles',
    'description': 'Another nice car',
    'price': '25000',
    })
    self.assertEqual(response.status_code, 201)
def test_get_vehicle_data(self):
    response = self.client.get('/vehicle_data/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 1)