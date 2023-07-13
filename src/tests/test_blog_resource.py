import unittest
from flask import Flask
from flask_restful import Api
from unittest.mock import MagicMock
from src.routes.blog_resource import BlogResource

class TestBlogResource(unittest.TestCase):
    def setUp(self):
        self.blog_repository = MagicMock()
        self.comment_repository = MagicMock()

        app = Flask(__name__)
        api = Api(app)

        api.add_resource(
            BlogResource,
            '/blogs',
            '/blogs/<int:id>',
            resource_class_args=[self.blog_repository, self.comment_repository]
        )

        self.client = app.test_client()

    def test_get(self):
        blog_id = 1
        blog = {'id': 1, 'title': 'Test Blog', 'content': 'Test Content', 'author': 'Test Author'}
        self.blog_repository.get_blog_by_id.return_value = blog
        expected_result = {'blog': blog}

        response = self.client.get(f'/blogs/{blog_id}')
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.blog_repository.get_blog_by_id.assert_called_once_with(blog_id)

    def test_get_not_found(self):
        blog_id = 1
        self.blog_repository.get_blog_by_id.return_value = None
        expected_result = {'message': 'Blog not found'}

        response = self.client.get(f'/blogs/{blog_id}')
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 404)
        self.blog_repository.get_blog_by_id.assert_called_once_with(blog_id)

    def test_get_all(self):
        blogs = [
            {'id': 1, 'title': 'Test Blog 1', 'content': 'Test Content 1', 'author': 'Test Author 1'},
            {'id': 2, 'title': 'Test Blog 2', 'content': 'Test Content 2', 'author': 'Test Author 2'},
        ]
        self.blog_repository.get_all_blogs.return_value = blogs
        expected_result = {'blogs': blogs}

        response = self.client.get('/blogs')
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.blog_repository.get_all_blogs.assert_called_once()

    def test_post(self):
        args = {'title': 'Test Blog', 'content': 'Test Content', 'author': 'Test Author'}
        created_blog = {'id': 1, 'title': 'Test Blog', 'content': 'Test Content', 'author': 'Test Author'}
        self.blog_repository.create_blog.return_value = created_blog
        expected_result = {'message': 'Blog created successfully', 'blog': created_blog}

        response = self.client.post('/blogs', json=args)
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 201)
        self.blog_repository.create_blog.assert_called_once_with(args['title'], args['content'], args['author'])

    def test_put(self):
        blog_id = 1
        args = {'title': 'Updated Blog', 'content': 'Updated Content', 'author': 'Updated Author'}
        existing_blog = {'id': 1, 'title': 'Test Blog', 'content': 'Test Content', 'author': 'Test Author'}
        updated_blog = {'id': 1, 'title': 'Updated Blog', 'content': 'Updated Content', 'author': 'Updated Author'}
        self.blog_repository.get_blog_by_id.return_value = existing_blog
        self.blog_repository.update_blog.return_value = True
        self.blog_repository.get_blog_by_id.return_value = updated_blog
        expected_result = {'message': 'Blog updated successfully', 'blog': updated_blog}

        response = self.client.put(f'/blogs/{blog_id}', json=args)
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.blog_repository.get_blog_by_id.assert_called_with(blog_id)
        self.blog_repository.update_blog.assert_called_once_with(blog_id, args['title'], args['content'], args['author'])

    def test_put_not_found(self):
        blog_id = 1
        args = {'title': 'Updated Blog', 'content': 'Updated Content', 'author': 'Updated Author'}
        self.blog_repository.get_blog_by_id.return_value = None
        expected_result = {'message': 'Blog not found'}

        response = self.client.put(f'/blogs/{blog_id}', json=args)
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 404)
        self.blog_repository.get_blog_by_id.assert_called_with(blog_id)
        self.blog_repository.update_blog.assert_not_called()

    def test_put_update_failed(self):
        blog_id = 1
        args = {'title': 'Updated Blog', 'content': 'Updated Content', 'author': 'Updated Author'}
        existing_blog = {'id': 1, 'title': 'Test Blog', 'content': 'Test Content', 'author': 'Test Author'}
        self.blog_repository.get_blog_by_id.return_value = existing_blog
        self.blog_repository.update_blog.return_value = False
        expected_result = {'message': 'Failed to update blog'}

        response = self.client.put(f'/blogs/{blog_id}', json=args)
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 500)
        self.blog_repository.get_blog_by_id.assert_called_once_with(blog_id)
        self.blog_repository.update_blog.assert_called_once_with(blog_id, args['title'], args['content'], args['author'])

    def test_delete(self):
        blog_id = 1
        self.blog_repository.delete_blog.return_value = True
        expected_result = {'message': 'Blog deleted successfully'}

        response = self.client.delete(f'/blogs/{blog_id}')
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)
        self.blog_repository.delete_blog.assert_called_once_with(blog_id)

    def test_delete_not_found(self):
        blog_id = 1
        self.blog_repository.delete_blog.return_value = False
        expected_result = {'message': 'Blog not found'}

        response = self.client.delete(f'/blogs/{blog_id}')
        result = response.get_json()
        status_code = response.status_code

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 404)
        self.blog_repository.delete_blog.assert_called_once_with(blog_id)


if __name__ == '__main__':
    unittest.main()
