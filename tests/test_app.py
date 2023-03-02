import unittest
import requests

class CrawlerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.url = 'https://www.cvbankas.lt?page='
    
    
    def test_download_url(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
    

    def test_download_content(self):
        response = requests.get(self.url)
        self.assertTrue(response.headers)
    

if __name__ == '__main__':
    unittest.main()