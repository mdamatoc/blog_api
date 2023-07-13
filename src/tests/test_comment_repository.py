import unittest
from src.repositories.comment_repository import CommentRepository

class CommentRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.comment_repository = CommentRepository()

    def test_get_comments_for_blog(self):
        # Test empty comment list
        comments = self.comment_repository.get_comments_for_blog(1)
        self.assertEqual(len(comments), 0)

        # Add comments to the repository
        comment1 = self.comment_repository.create_comment(1, "Comment 1", "Author 1")
        comment2 = self.comment_repository.create_comment(1, "Comment 2", "Author 2")

        # Test if all comments for the specific blog are returned
        comments = self.comment_repository.get_comments_for_blog(1)
        self.assertEqual(len(comments), 2)

    def test_get_comment(self):
        # Add a comment to the repository
        comment = self.comment_repository.create_comment(1, "Comment", "Author")

        # Test getting the comment
        retrieved_comment = self.comment_repository.get_comment(1, comment['comment_id'])
        self.assertEqual(retrieved_comment, comment)

        # Test getting a non-existent comment
        non_existent_comment = self.comment_repository.get_comment(1, 999)
        self.assertIsNone(non_existent_comment)

    def test_create_comment(self):
        # Test creating a new comment
        comment = self.comment_repository.create_comment(1, "New Comment", "New Author")
        self.assertIsNotNone(comment)
        self.assertEqual(comment['blog_id'], 1)
        self.assertEqual(comment['content'], "New Comment")
        self.assertEqual(comment['author'], "New Author")

        # Test if the comment is added to the repository
        comments = self.comment_repository.get_comments_for_blog(1)
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0], comment)

    def test_update_comment(self):
        # Add a comment to the repository
        comment = self.comment_repository.create_comment(1, "Comment", "Author")

        # Test updating the comment
        updated = self.comment_repository.update_comment(1, comment['comment_id'], "Updated Comment", "Updated Author")
        self.assertTrue(updated)

        # Test if the comment is updated in the repository
        updated_comment = self.comment_repository.get_comment(1, comment['comment_id'])
        self.assertEqual(updated_comment['content'], "Updated Comment")
        self.assertEqual(updated_comment['author'], "Updated Author")

    def test_delete_comment(self):
        # Add a comment to the repository
        comment = self.comment_repository.create_comment(1, "Comment", "Author")

        # Test deleting the comment
        deleted = self.comment_repository.delete_comment(1, comment['comment_id'])
        self.assertTrue(deleted)

        # Test if the comment is removed from the repository
        deleted_comment = self.comment_repository.get_comment(1, comment['comment_id'])
        self.assertIsNone(deleted_comment)

    def test_delete_non_existent_comment(self):
        # Test deleting a non-existent comment
        deleted = self.comment_repository.delete_comment(1, 999)
        self.assertFalse(deleted)

if __name__ == '__main__':
    unittest.main()
