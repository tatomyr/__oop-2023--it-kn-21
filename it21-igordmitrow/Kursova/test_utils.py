import unittest
from service import DeezerService
import os

class TestDeezerService(unittest.TestCase):

    def test_download_success(self):
        # Тест успішного завантаження
        
        expectation = os.path.dirname(__file__) + '/songs/Believe.mp3'
        deezer = DeezerService()
        search = deezer.search_music('Believe')
        track = search[0]
        result = deezer.start_downloading(track)
        
        self.assertEqual(result, expectation)
        
    def test_download_failure(self):
        # Тест невдалого завантаження 
        deezer = DeezerService()
        result = deezer.start_downloading('123', t='id')
        
        self.assertFalse(result)
       
if __name__ == '__main__':
    unittest.main()