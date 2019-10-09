import json
from django.test import TestCase, Client

from .models import Author

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="Author")

    def test_create_author(self):
        c = Client()
        body = dict()
        body['query'] = '''{
            authors {
                id
                name
            }
        }'''
        response = c.post('/graphql/', json.dumps(body), content_type='application/json')
        response_content = json.loads(response.content)
        self.assertIn('data', response_content)
