from django.test import TestCase
from django.contrib.auth.models import User
from comments.models import Comment
from issues.models import Issue

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.issue = Issue.objects.create(title='Test Issue', description='Test Issue Description')
        self.comment = Comment.objects.create(
            comment='This is a test comment',
            owner=self.user,
            issue_id=self.issue
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.comment, 'This is a test comment')
        self.assertFalse(self.comment.resolved)
        self.assertEqual(self.comment.owner.username, 'testuser')
        self.assertEqual(self.comment.issue_id, self.issue)

    def test_comment_str(self):
        self.assertEqual(str(self.comment), "testuser's comments")

    def test_comment_ordering(self):
        comment2 = Comment.objects.create(
            comment='Another test comment',
            owner=self.user,
            issue_id=self.issue
        )
        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment2)
        self.assertEqual(comments[1], self.comment)