import unittest

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from blog.models import Post


class PostTest(TestCase):
    def test_create_post(self):
        # Create the post
        post = Post()

        # Set the attributes
        u = User()
        u.save()
        post.author = u
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.published_date = timezone.now()
        post.created_date = timezone.now()

        # Save it
        post.save()

        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Check attributes
        self.assertEquals(only_post.author, u)
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.published_date.day, post.published_date.day)
        self.assertEquals(only_post.published_date.month, post.published_date.month)
        self.assertEquals(only_post.published_date.year, post.published_date.year)
        self.assertEquals(only_post.published_date.hour, post.published_date.hour)
        self.assertEquals(only_post.published_date.minute, post.published_date.minute)
        self.assertEquals(only_post.published_date.second, post.published_date.second)
        self.assertEquals(only_post.created_date.day, post.created_date.day)
        self.assertEquals(only_post.created_date.month, post.created_date.month)
        self.assertEquals(only_post.created_date.year, post.created_date.year)
        self.assertEquals(only_post.created_date.hour, post.created_date.hour)
        self.assertEquals(only_post.created_date.minute, post.created_date.minute)
        self.assertEquals(only_post.created_date.second, post.created_date.second)


if __name__ == '__main__':
    unittest.main(verbosity=2)
