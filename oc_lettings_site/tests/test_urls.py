from django.test import SimpleTestCase
from django.urls import reverse, resolve
from oc_lettings_site.views import index


class LettingUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func, index)
