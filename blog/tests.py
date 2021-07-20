from django.test import TestCase
import logging
from django.urls import reverse
from .models import Blog

logger = logging.getLogger('django')

class MyTest(TestCase):
    
    def setUp(self):
        self.b = Blog.objects.all()
    
    def test_detail_of_blog(self):
        response = self.client.get(reverse('list_blog'))
        print(self.b)
        # self.assertContains(response, self.b[0])

    def test_name(self):
        print("this is test name =========")
        self.assertEqual(1, 1)
        self.assertIn(1, [1,2,3,4])

    def test_list(self):
        print("this is test list =========")
        self.assertIn(1, [1,2,3,4])
    
    def test_create_object(self):
        blog = Blog.objects.create(title='This is the title', content="this is the content")
        self.assertEqual('This is the title', blog.title)
        self.assertIn(blog, Blog.objects.all())

    def tearDown(self):
        print("this teardown runs ----------")


class MyTest2(TestCase):

    def test_equal(self):
        self.assertEqual(1, 1)

    def test_list(self):
        self.assertIn(1, [1,2,3,4])
    
    def test_check_root_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


# test*.py
# test_modle.py
# tests.py
# test_view.py