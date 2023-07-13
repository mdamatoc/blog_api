from flask_restful import Resource, reqparse

class CommentResource(Resource):
    def __init__(self, blog_repository, comment_repository):
        self.blog_repository = blog_repository
        self.comment_repository = comment_repository
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('content', type=str, required=True, help='Content is required.')
        self.parser.add_argument('author', type=str, required=True, help='Author is required.')

    def get(self, blog_id, comment_id=None):
        """Get a specific comment or all comments of a specific blog"""
        if comment_id:
            comment = self.comment_repository.get_comment(blog_id, comment_id)
            if comment:
                return {'comment': comment}, 200
            return {'message': 'Comment not found'}, 404
        else:
            comments = self.comment_repository.get_comments_for_blog(blog_id)
            return {'comments': comments}, 200

    def post(self, blog_id):
        """Create a new comment for a specific blog"""
        args = self.parser.parse_args()
        comment = self.comment_repository.create_comment(blog_id, args['content'], args['author'])
        return {'message': 'Comment created successfully', 'comment': comment}, 201

    def put(self, blog_id, comment_id):
        """Update a specific comment"""
        args = self.parser.parse_args()
        success = self.comment_repository.update_comment(blog_id, comment_id, args['content'], args['author'])
        if success:
            comment = self.comment_repository.get_comment(blog_id, comment_id)
            return {'message': 'Comment updated successfully', 'comment': comment}, 200
        return {'message': 'Comment not found'}, 404

    def delete(self, blog_id, comment_id):
        """Delete a specific comment"""
        success = self.comment_repository.delete_comment(blog_id, comment_id)
        if success:
            return {'message': 'Comment deleted successfully'}, 200
        return {'message': 'Comment not found'}, 404
