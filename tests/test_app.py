import unittest
import requests

class CrawlerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.url = 'https://www.cvbankas.lt?page='
    
    
    def test_download_url(self):
        self.response = requests.get(self.url)
        self.assertEqual(self.response.status_code, 200)


    def test_download_headers(self):
        self.response = requests.get(self.url)
        self.assertTrue(self.response.headers)


if __name__ == '__main__':
    unittest.main()