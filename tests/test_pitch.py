import unittest
from app.models import Pitch,User,Pitch
from app import db

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, pitch_title = 'Python', pitch_content = 'Programming language that helps to build application', category = 'courses pitches', like = 3, dislike = 0)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

if __name__ == '__main__':
    unittest.main()

