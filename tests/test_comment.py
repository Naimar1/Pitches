# import unittest
# from app.models import Comment,User

# class CommentModelTest(unittest.TestCase):

#     def setUp(self):
#         self.new_comment = Comment(body = 'very nice progress!!')

#     def tearDown(self):
#         Coment.query.delete()
       

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_comment, Comment))

#     def test_save_comment(self):
#         self.new_comment.save_comment()
#         self.assertTrue(len(Comment.query.all())>0

#     def test_get_comment_by_id(self):

#         self.new_comment.save_comment()
#         got_comments = Comment.get_comments()
#         self.assertTrue(len(got_comments) == 1)

# if __name__ == '__main__':
#     unittest.main()

from app.models import Comment, User, Pitch
from app import db
import unittest


class CommentModelTest(unittest.TestCase):
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
        self.new_comment = Comment(
            id=1,
            comment='Test comment',
            comment_writer='Good course'
            user=self.user_James,
            pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'Test comment')
        self.assertEquals(self.new_comment.comment, 'Good course')
        self.assertEquals(self.new_comment.user, self.user_James)
        self.assertEquals(self.new_comment.pitch, self.new_pitch)
