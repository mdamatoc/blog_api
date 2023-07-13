import unittest
from src.repositories.blog_repository import BlogRepository

class BlogRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.blog_repository = BlogRepository()

    def test_get_all_blogs(self):
        # Test empty blog list
        blogs = self.blog_repository.get_all_blogs()
        self.assertEqual(len(blogs), 0)

        # Add blogs to the repository
        blog1 = self.blog_repository.create_blog("Blog 1", "Content 1", "Author 1")
        blog2 = self.blog_repository.create_blog("Blog 2", "Content 2", "Author 2")

        # Test if all blogs are returned
        blogs = self.blog_repository.get_all_blogs()
        self.assertEqual(len(blogs), 2)

    def test_get_blog_by_id(self):
        # Add a blog to the repository
        blog = self.blog_repository.create_blog("Blog", "Content", "Author")

        # Test getting the blog by ID
        retrieved_blog = self.blog_repository.get_blog_by_id(blog['id'])
        self.assertEqual(retrieved_blog, blog)

        # Test getting a non-existent blog
        non_existent_blog = self.blog_repository.get_blog_by_id(999)
        self.assertIsNone(non_existent_blog)

    def test_create_blog(self):
        # Test creating a new blog
        blog = self.blog_repository.create_blog("New Blog", "New Content", "New Author")
        self.assertIsNotNone(blog)
        self.assertEqual(blog['title'], "New Blog")
        self.assertEqual(blog['content'], "New Content")
        self.assertEqual(blog['author'], "New Author")

        # Test if the blog is added to the repository
        blogs = self.blog_repository.get_all_blogs()
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0], blog)

    def test_update_blog(self):
        # Add a blog to the repository
        blog = self.blog_repository.create_blog("Blog", "Content", "Author")

        # Test updating the blog
        updated = self.blog_repository.update_blog(blog['id'], "Updated Blog", "Updated Content", "Updated Author")
        self.assertTrue(updated)

        # Test if the blog is updated in the repository
        updated_blog = self.blog_repository.get_blog_by_id(blog['id'])
        self.assertEqual(updated_blog['title'], "Updated Blog")
        self.assertEqual(updated_blog['content'], "Updated Content")
        self.assertEqual(updated_blog['author'], "Updated Author")

    def test_delete_blog(self):
        # Add a blog to the repository
        blog = self.blog_repository.create_blog("Blog", "Content", "Author")

        # Test deleting the blog
        deleted = self.blog_repository.delete_blog(blog['id'])
        self.assertTrue(deleted)

        # Test if the blog is removed from the repository
        deleted_blog = self.blog_repository.get_blog_by_id(blog['id'])
        self.assertIsNone(deleted_blog)

    def test_delete_non_existent_blog(self):
        # Test deleting a non-existent blog
        deleted = self.blog_repository.delete_blog(999)
        self.assertFalse(deleted)

if __name__ == '__main__':
    unittest.main()
