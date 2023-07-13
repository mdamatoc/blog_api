class CommentRepository:
    def __init__(self):
        self.comments = []
        self.next_id = 1

    def get_comments_for_blog(self, blog_id):
        """Get all comments for a specific blog"""
        return [comment for comment in self.comments if comment['blog_id'] == blog_id]

    def get_comment(self, blog_id, comment_id):
        """Get a specific comment"""
        for comment in self.comments:
            if comment['blog_id'] == blog_id and comment['comment_id'] == comment_id:
                return comment
        return None

    def create_comment(self, blog_id, content, author):
        """Create a new comment for a specific blog"""
        comment = {
            'blog_id': blog_id,
            'comment_id': self.next_id,
            'content': content,
            'author': author
        }

        self.next_id += 1

        self.comments.append(comment)
        return comment

    def update_comment(self, blog_id, comment_id, content, author):
        """Update a specific comment"""
        for comment in self.comments:
            if comment['blog_id'] == blog_id and comment['comment_id'] == comment_id:
                comment['content'] = content
                comment['author'] = author
                return True
        return False

    def delete_comment(self, blog_id, comment_id):
        """Delete a specific comment"""
        for comment in self.comments:
            if comment['blog_id'] == blog_id and comment['comment_id'] == comment_id:
                self.comments.remove(comment)
                return True
        return False
