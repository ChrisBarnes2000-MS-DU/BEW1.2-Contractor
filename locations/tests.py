# Locations/tests.py
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from locations.models import Page

class LocationTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        user = User()
        user.save()

        # Create and save a new page to the test database.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page",
                            content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )

class PageDetailViewTests(TestCase):
    def test_slug(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        page1 = Page.objects.create(
            title="My Test Page", content="test", author=user)
        page2 = Page.objects.create(
            title="Another Test Page", content="test", author=user)

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page1.slug, "my-test-page")
        self.assertEqual(page2.slug, "another-test-page")

        url1 = reverse('wiki-details-page', args=[page1.slug])
        url2 = reverse('wiki-details-page', args=[page2.slug])

        # Issue a GET request to the MakeWiki Detail page.
        # When we make a request, we get a response back.
        response1 = self.client.get(url1)
        response2 = self.client.get(url2)

        # Check that the response is 200 OK.
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

class PageCreateViewTest(TestCase):
    def test(self):
        user = User.objects.create()

        # Make some test data to be sent through the create page.
        data = {"title": "my-test-page", "content": "test", "author": user}

        response = self.client.post('wiki-create-page', data=data)

        self.assertEqual(response.status_code, 302)
