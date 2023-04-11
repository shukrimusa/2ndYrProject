from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.


class SearchTest(TestCase):
    def test_search_results_listView(self):
        response = self.client.get(reverse('search:searchResult'), {'q':'Keyboard'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Keyboard')
        self.assertTemplateUsed(response, 'search.html')

# Issue
# django.urls.exceptions.NoReverseMatch: Reverse for 'searchResult' not found. 'searchResult' is not a valid view function or pattern name.
# solved