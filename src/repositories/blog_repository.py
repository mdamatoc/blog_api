class BlogRepository:
    def __init__(self):
        self.blogs = []
        self.next_id = 1

    def get_all_blogs(self):
        """Get all blogs"""
        return self.blogs

    def get_blog_by_id(self, blog_id):
        """Get a specific blog by ID"""
        for blog in self.blogs:
            if blog['id'] == blog_id:
                return blog
        return None

    def create_blog(self, title, content, author):
        """Create a new blog"""
        blog = {'id': self.next_id, 'title': title, 'content': content, 'author': author}
        self.blogs.append(blog)
        self.next_id += 1
        return blog

    def update_blog(self, blog_id, title, content, author):
        """Update a specific blog by ID"""
        blog = self.get_blog_by_id(blog_id)
        if blog:
            blog['title'] = title
            blog['content'] = content
            blog['author'] = author
            return True
        return False

    def delete_blog(self, blog_id):
        """Delete a specific blog by ID"""
        blog = self.get_blog_by_id(blog_id)
        if blog:
            self.blogs.remove(blog)
            return True
        return False