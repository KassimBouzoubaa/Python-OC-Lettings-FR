from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index, letting

class LettingUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('lettings_index')
        self.assertEqual(resolve(url).func, index)
    
    def test_letting_url_resolves(self):
        url = reverse('letting', args=[1])
        self.assertEqual(resolve(url).func, letting)
