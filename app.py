from flask import Flask
from flask_restful import Api
from src.routes.blog_resource import BlogResource
from src.routes.comment_resource import CommentResource
from src.repositories.blog_repository import BlogRepository
from src.repositories.comment_repository import CommentRepository

app = Flask(__name__)
api = Api(app)

# Instantiate repositories
blog_repository = BlogRepository()
comment_repository = CommentRepository()

# Add resources (API endpoints)
api.add_resource(BlogResource, '/blogs', '/blogs/<int:id>', resource_class_args=[blog_repository, comment_repository])
api.add_resource(CommentResource, '/blogs/<int:blog_id>/comments', '/blogs/<int:blog_id>/comments/<int:comment_id>',
                 resource_class_args=[blog_repository, comment_repository])


if __name__ == '__main__':
    app.run(debug=True)
