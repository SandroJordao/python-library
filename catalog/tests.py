from rest_framework.test import APITestCase, APIClient
from rest_framework.response import Response
from rest_framework import status
from .models import Authors, Books


class TestApiAuthors(APITestCase):
    """ 
    Authors
    Test suite for the api views. 
    """

    def setUp(self):
        self.url = '/authors/'
        self.client = APIClient()
        Authors.objects.create(name='Stephen King')

    def test_api_create_author(self):
        """ 
        Test the api can create a given author. 
        """
        new_author = {'name': 'Agatha Christie'}
        response = self.client.post(self.url, new_author, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_author['name'])

    def test_api_get_author(self):
        """ 
        Test the api can get a given author. 
        """
        author = Authors.objects.get(id=1)
        response = self.client.get(
            self.url, kwargs={'pk': author.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, author)

    def test_api_update_author(self):
        """
        Test the api can update a given author.
        """
        author = Authors.objects.get(id=1)
        update_author = {'name': 'Author Update'}
        patch = "{}{}/".format(self.url, author.id)
        response = self.client.put(patch, update_author, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_author['name'])

    def test_api_delete_author(self):
        """
        Test the api can delete a author.
        """
        author = Authors.objects.get()
        patch = "{}{}/".format(self.url, author.id)
        response = self.client.delete(patch, format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class TestApiBooks(APITestCase):
    """ 
    Books
    Test suite for the api views. 
    """

    def setUp(self):
        self.url = '/books/'
        self.client = APIClient()
        Authors.objects.create(name='Stephen King')
        Books.objects.create(name='Christine', edition=1,
                             publication_year=1983)

    def test_api_create_book(self):
        """ 
        Test the api can create a given book. 
        """
        new_book = {'name': 'The Shining', 'edition': 1,
                    'publication_year': 1977, 'authors': [1]}
        response = self.client.post(self.url, new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], new_book['name'])
        self.assertEqual(response.data['edition'], new_book['edition'])
        self.assertEqual(
            response.data['publication_year'], new_book['publication_year'])

    def test_api_get_book(self):
        """ 
        Test the api can get a given book. 
        """
        book = Books.objects.get(id=1)
        response = self.client.get(
            self.url, kwargs={'pk': book.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, book)

    def test_api_update_book(self):
        """
        Test the api can update a given book.
        """
        book = Books.objects.get(id=1)
        update_book = {'name': 'Name Book Update'}
        patch = "{}{}/".format(self.url, book.id)
        response = self.client.patch(patch, update_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_book['name'])

    def test_api_delete_book(self):
        """
        Test the api can delete a book.
        """
        book = Books.objects.get()
        patch = "{}{}/".format(self.url, book.id)
        response = self.client.delete(patch, format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
