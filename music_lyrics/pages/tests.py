from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
from .models import Page

class PageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.post = Page.objects.create(
            title = 'A good title', 
            video_url = "Nice body content",
            user = self.user,
            lyrics = "lorem some text here"
        )

    