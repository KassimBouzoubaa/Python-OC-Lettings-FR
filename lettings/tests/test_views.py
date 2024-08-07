from django.test import TestCase, Client
from django.urls import reverse
from lettings.models import Address, Letting

class LettingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Springfield',
            state='IL',
            zip_code=62701,
            country_iso_code='USA'
        )
        self.letting = Letting.objects.create(
            title='Cozy Apartment',
            address=self.address
        )
    
    def test_index_view(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lettings')
    
    def test_letting_view(self):
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cozy Apartment')
