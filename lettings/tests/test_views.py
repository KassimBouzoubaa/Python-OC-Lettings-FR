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
    
    def test_letting_view_with_error(self):
        # Simulez un ID de letting qui n'existe pas
        non_existent_id = 9999
        response = self.client.get(reverse('letting', args=[non_existent_id]))

        # Vérifiez que la réponse a un code de statut 404
        self.assertEqual(response.status_code, 404)

        # Vérifiez que le message d'erreur attendu est contenu dans la réponse
        self.assertContains(response, 'Oups ! Page non trouvée', status_code=404)