# import unittest
# from app.models import Pitch

# class PitchModelTest(unittest.TestCase):

#     def setUp(self):
#         self.new_pitch = Pitch(id = 1, title = 'Python', pitch_content = 'Programming language that helps to build application', category = 'courses pitches', like = 3, dislike = 0)


#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_pitch, Pitch))

#     def test_save_comment(self):
#         self.new_comment.save_comment()
#         self.assertTrue(len(Comment.query.all())>0)

# if __name__ == '__main__':
#     unittest.main()

from app.models import Comment, User, Pitch
from app import db
import unittest


class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(
            username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(
            id=1,
            pitch_title='Test',
            pitch_content='Programming language',
            category="course",
            user=self.user_James,
            likes=0,
            dislikes=0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title, 'Test')
        self.assertEquals(self.new_pitch.pitch_content, 'Programming language')
        self.assertEquals(self.new_pitch.category, "course")
        self.assertEquals(self.new_pitch.user, self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)
