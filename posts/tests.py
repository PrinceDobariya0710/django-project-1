from django.test import TestCase
from posts.models import Post

# Create your tests here.
class PostTestCase(TestCase):
    
    def setUp(self):
        super().setUp()
        self.post = Post.objects.create(
            title="Test Post",
            author="Test author",
            content="Test content"
        ) 
    def test_home_page(self):   
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"List of Posts")
        self.assertTemplateUsed(response,'index.html')

    def test_post_creation(self):
        post_to_test = Post.objects.get(pk=1)
        post_title = f"{post_to_test.title}"
        self.assertEqual(self.post.title,post_title)
        self.assertEqual(self.post.author,"Test author")
        self.assertEqual(self.post.content,"Test content")
