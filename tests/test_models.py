import unittest

class PostTestCase(unittest.TestCase):
    
    def setUp(self):
        self.id='123'
        self.salary=[1200, 1800]
        self.applicants='10'
        
    def test_keys(self):
        self.assertTrue(isinstance(self.id, str))
        self.assertTrue(isinstance(self.salary, list))
        self.assertTrue(isinstance(self.applicants, str))  
        
    # def test_data_dict(self):
    #     self.assertEqual(data_dict(), dict)
          
    # def setUp(self):
    #     self.post = Post(
    #         id='123',
    #         url='http://example.com',
    #         img_url='http://example.com/image.jpg',
    #         position='Software Developer',
    #         company='Acme Inc.',
    #         city='New York',
    #         salary=[1200, 1800],
    #         post_date='2022-01-01',
    #         upload_post='2022-01-02',
    #         description='This is a job description.',
    #         applicants_value=[10]
        # )
        # def setUp(self):
    #     self.id= '123'
    #     self.url='http://example.com',
    #     self.img_url='http://example.com/image.jpg',
    #     self.position='Software Developer',
    #     self.company='Acme Inc.',
    #     self.city='New York',
    #     self.salary=[1200, 1800],
    #     self.post_date='2022-01-01',
    #     self.upload_post='2022-01-02',
    #     self.description='This is a job description.',
    #     self.applicants_value=[10]
    # def test_data_dict(self):
    #     expected = {
    #         'post_id': '123',
    #         'post_url': 'http://example.com',
    #         'img_url': 'http://example.com/image.jpg',
    #         'position': 'Software Developer',
    #         'company': 'Acme Inc.',
    #         'city': 'New York',
    #         'salary': [1200, 1800],
    #         'post_date': '2022-01-01',
    #         'upload_post': '2022-01-02',
    #         'description': 'This is a job description.',
    #         'applicants_value': [10]
    #     }
        
    #     self.assertEqual(self.post.data_dict(), expected) 
        
if __name__ == '__main__':
    unittest.main()

