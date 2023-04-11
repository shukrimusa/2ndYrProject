from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView, ContactPageView

# SimpleTest did not work here!


class PageTests(TestCase):

    def setUp(self):
        homeUrl = reverse('home')
        self.homeResp = self.client.get(homeUrl)

        aboutUrl = reverse('about')
        self.aboutResp = self.client.get(aboutUrl)

        contactUrl = reverse('contact')
        self.contactResp = self.client.get(contactUrl)

    # Home Page tests
    def test_homepage_status_code(self):
        self.assertEqual(self.homeResp.status_code, 200)

    def test_homepage_templage(self):
        self.assertTemplateUsed(self.homeResp, 'home.html')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

    # About page tests
    def test_aboutpage_status_code(self):
        self.assertEqual(self.aboutResp.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.aboutResp, 'about.html')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

    # Contact page tests
    def test_contactpage_status_code(self):
        self.assertEqual(self.contactResp.status_code, 200)

    def test_contactpage_template(self):
        self.assertTemplateUsed(self.contactResp, 'contact.html')

    def test_contactpage_url_resolves_contactpageview(self):
        view = resolve('/contact us/')
        self.assertEqual(
            view.func.__name__,
            ContactPageView.as_view().__name__
        )
