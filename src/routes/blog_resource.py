from flask_restful import Resource, reqparse

class BlogResource(Resource):
    def __init__(self, blog_repository, comment_repository):
        self.blog_repository = blog_repository
        self.comment_repository = comment_repository
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help='Title is required.')
        self.parser.add_argument('content', type=str, required=True, help='Content is required.')
        self.parser.add_argument('author', type=str, required=True, help='Author is required.')

    def get(self, id:int or None=None):
        """Get all blogs or a specific blog by ID"""
        if id is None:
            blogs = self.blog_repository.get_all_blogs()
            return {'blogs': blogs}, 200
        else:
            blog = self.blog_repository.get_blog_by_id(id)
            if blog:
                return {'blog': blog}, 200
            else:
                return {'message': 'Blog not found'}, 404

    def post(self):
        """Create a new blog"""
        args = self.parse_args()
        blog = self.blog_repository.create_blog(args['title'], args['content'], args['author'])
        return {'message': 'Blog created successfully', 'blog': blog}, 201
    
    def put(self, id: int):
        """Update a specific blog by ID"""
        args = self.parse_args()
        blog = self.blog_repository.get_blog_by_id(id)
        if blog:
            updated = self.blog_repository.update_blog(id, args['title'], args['content'], args['author'])
            if updated:
                updated_blog = self.blog_repository.get_blog_by_id(id)
                return {'message': 'Blog updated successfully', 'blog': updated_blog}, 200
            else:
                return {'message': 'Failed to update blog'}, 500
        else:
            return {'message': 'Blog not found'}, 404
        
    def delete(self, id: int):
        """Delete a specific blog by ID"""
        deleted = self.blog_repository.delete_blog(id)
        if deleted:
            return {'message': 'Blog deleted successfully'}, 200
        else:
            return {'message': 'Blog not found'}, 404

    def parse_args(self):
        """Parse and return the request arguments"""
        return self.parser.parse_args()
