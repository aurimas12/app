import unittest
from app import Crawler

class TestCrawler(unittest.TestCase):
    
    def test_download_url(self):
        downl_url=Crawler('https://www.cvbankas.lt?page=')
        self.assertTrue(downl_url.download_url())

if __name__ == '__main__':
    unittest.main()