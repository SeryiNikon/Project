import unittest

from django.test import RequestFactory, TestCase

from blog.views import PostDetailView


class PostListViewsTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view = PostDetailView()
        view.setup(request)

if __name__ == '__main__':
    unittest.main(verbosity=2)
