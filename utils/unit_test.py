import unittest
from app import Crawler

class TestCrawler(unittest.TestCase):
    
    def test_download_url(self):
        down=Crawler(url='https://www.cvbankas.lt?page=')
        self.assertEqual(down.download_url())

if __name__ == '__main__':
    unittest.main()