from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(
            user=self.user, favorite_city="Springfield"
        )

    def test_index_view(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")

    def test_profile_view(self):
        response = self.client.get(reverse("profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Springfield")
