import unittest
import mock
import requests
from src.dataseeker_luanramos.entity import RequestEntity, TypeRequestEnum
from src.dataseeker_luanramos.main import DataSeeker


class TestDataSeeker(unittest.TestCase):
    def test_create_request(self):
        url = 'https://example.com'
        metadata = {'type_request': 'REST'}
        request = DataSeeker.create_request(url, metadata)
        self.assertIsInstance(request, RequestEntity)
        self.assertEqual(request.url, url)
        self.assertEqual(request.type_request, TypeRequestEnum.REST)
        self.assertIsNone(request.operation)
        self.assertIsNone(request.headers)
        self.assertIsNone(request.body)

    def test_create_request_no_url(self):
        url = None
        metadata = {'type_request': 'REST'}
        with self.assertRaises(Exception) as context:
            DataSeeker.create_request(url, metadata)
        self.assertEqual(str(context.exception), "Cant create a request without URL")

    @mock.patch('requests.get')
    def test_handle_get_request(self, mock_get):
        request = RequestEntity('https://example.com', TypeRequestEnum.REST, 'GET',
                                headers={'Content-Type': 'application/json'})
        data_seeker = DataSeeker(request)
        data_seeker.handle()
        mock_get.assert_called_with(request.url, headers=request.headers)

    @mock.patch('requests.post')
    def test_handle_post_request(self, mock_post):
        request = RequestEntity('https://example.com', TypeRequestEnum.REST, 'POST',
                                headers={'Content-Type': 'application/json'}, body={'name': 'John Doe'})
        data_seeker = DataSeeker(request)
        data_seeker.handle()
        mock_post.assert_called_with(request.url, headers=request.headers, json=request.body)
