# wiki/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page



class WikiTestCase(TestCase):


    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # Create and save a new page to the test database.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()





        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")



    def test_details_page(self):
        user = User.objects.create()

        page = Page.objects.create(title='Test Title', content='Test Content', author=user)

        page.save()

        page_path = '/' + page.slug + '/'

        response = self.client.get(page_path)

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, 'Test Title')


    def test_page_edit(self):

        user = User.objects.create_user(username='testname', password='123')

        self.client.login(username='testname', password='123')

        page = Page.objects.create(title='test title', author=user, content='test content')

        page.save()

        post_data = {
            'title': 'changed title',
            'author': user.id,
            'content': 'changed content'
        }

        page_path = '/' + page.slug + '/'

        response = self.client.post(page_path, post_data)


        self.assertEqual(response.status_code, 302)

        updated_page = Page.objects.get(title='changed title')

        self.assertEqual(updated_page.title, 'changed title')

