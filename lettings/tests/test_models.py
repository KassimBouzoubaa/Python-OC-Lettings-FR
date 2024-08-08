from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Springfield",
            state="IL",
            zip_code=62701,
            country_iso_code="USA",
        )

    def test_address_str(self):
        self.assertEqual(str(self.address), "123 Main Street")


class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Springfield",
            state="IL",
            zip_code=62701,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Cozy Apartment", address=self.address
        )

    def test_letting_str(self):
        self.assertEqual(str(self.letting), "Cozy Apartment")
