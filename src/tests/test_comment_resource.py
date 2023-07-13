import unittest
from unittest.mock import MagicMock
from src.routes.comment_resource import CommentResource

class TestCommentResource(unittest.TestCase):
    def setUp(self):
        self.blog_repository = MagicMock()
        self.comment_repository = MagicMock()
        self.comment_resource = CommentResource(self.blog_repository, self.comment_repository)

    def test_get(self):
        blog_id = 1
        comments = [
            {'id': 1, 'blog_id': 1, 'content': 'Comment 1', 'author': 'John Doe'},
            {'id': 2, 'blog_id': 1, 'content': 'Comment 2', 'author': 'Jane Smith'},
        ]
        self.comment_repository.get_comments_for_blog.return_value = comments
        expected_result = {'comments': comments}
        result, status_code = self.comment_resource.get(blog_id)
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.comment_repository.get_comments_for_blog.assert_called_once_with(blog_id)

    def test_get_with_comment_id(self):
        blog_id = 1
        comment_id = 2
        comment = {'id': 2, 'blog_id': 1, 'content': 'Comment 2', 'author': 'Jane Smith'}
        self.comment_repository.get_comment.return_value = comment
        expected_result = {'comment': comment}
        result, status_code = self.comment_resource.get(blog_id, comment_id)
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.comment_repository.get_comment.assert_called_once_with(blog_id, comment_id)
        self.comment_repository.get_comments_for_blog.assert_not_called()

    def test_get_with_comment_id_not_found(self):
        blog_id = 1
        comment_id = 3
        self.comment_repository.get_comment.return_value = None
        expected_result = {'message': 'Comment not found'}
        result, status_code = self.comment_resource.get(blog_id, comment_id)
        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 404)
        self.comment_repository.get_comment.assert_called_once_with(blog_id, comment_id)
        self.comment_repository.get_comments_for_blog.assert_not_called()

if __name__ == '__main__':
    unittest.main()
