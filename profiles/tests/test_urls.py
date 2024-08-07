from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index, profile

class ProfileUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('profiles_index')
        self.assertEqual(resolve(url).func, index)
    
    def test_profile_url_resolves(self):
        url = reverse('profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)
