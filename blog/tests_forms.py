from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    """ tests for the blog post form """

    def test_title_is_required(self):
        """ test to see if blog post title field is required"""
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title',
                      form.errors.keys())
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')

    def test_content_is_required(self):
        """ test to see if blog post content field is required"""
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content',
                      form.errors.keys())
        self.assertEqual(
            form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        """
        check the field only displays certain fields
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'content'])
